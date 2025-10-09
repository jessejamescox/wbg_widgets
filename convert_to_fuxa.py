#!/usr/bin/env python3
"""
Convert all SVG widgets to FUXA format:
1. Change width and height to 100%
2. Replace script section with FUXA format (export markers, init(), update(), putValue())
"""

import os
import re
from pathlib import Path

def convert_svg_to_fuxa(file_path):
    """Convert a single SVG file to FUXA format"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Step 1: Change width and height to 100%
    # Match width="number" or width='number'
    content = re.sub(r'\swidth=["\'][\d.]+["\']', ' width="100%"', content)
    content = re.sub(r'\sheight=["\'][\d.]+["\']', ' height="100%"', content)

    # Step 2: Find and analyze the script section
    script_pattern = r'<script[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</script>'
    script_match = re.search(script_pattern, content, re.DOTALL)

    if not script_match:
        print(f"  ⚠️  No script found in {file_path.name}")
        return False

    script_content = script_match.group(1)

    # Check if already converted
    if '//!export-start' in script_content:
        print(f"  ✓  Already converted: {file_path.name}")
        return False

    # Step 3: Analyze variables to export
    # Find var declarations
    var_pattern = r'^\s*var\s+(\w+)\s*=\s*([^;]+);(?:\s*//\s*(.*))?'
    variables = []

    for match in re.finditer(var_pattern, script_content, re.MULTILINE):
        var_name = match.group(1)
        var_value = match.group(2).strip()
        var_comment = match.group(3) if match.group(3) else ""

        # Determine variable type based on value
        if var_value in ['true', 'false'] or 'bool' in var_comment.lower():
            var_type = '_pb_'  # boolean
        elif var_value.startswith('"') or var_value.startswith("'") or 'string' in var_comment.lower():
            var_type = '_ps_'  # string
        else:
            var_type = '_pn_'  # number (default)

        # Skip internal variables (like rotation, animationId)
        skip_vars = ['rotation', 'animationId', 'animationFrame']
        if var_name not in skip_vars:
            variables.append({
                'name': var_name,
                'new_name': var_type + var_name,
                'value': var_value,
                'comment': var_comment,
                'type': var_type
            })

    if not variables:
        print(f"  ⚠️  No variables to export in {file_path.name}")
        return False

    # Step 4: Build new script content

    # Export section
    export_lines = ['//!export-start']
    for var in variables:
        comment = '  // ' + var['comment'] if var['comment'] else ''
        export_lines.append(f"let {var['new_name']} = {var['value']};{comment}")
    export_lines.append('//!export-end')
    export_section = '\n'.join(export_lines)

    # Find the main update/render function
    update_func_pattern = r'function\s+(\w*update\w*|render)\s*\([^)]*\)\s*\{'
    update_match = re.search(update_func_pattern, script_content, re.IGNORECASE)
    update_func_name = update_match.group(1) if update_match else 'updateWidget'

    # Replace variable references in script
    modified_script = script_content
    for var in variables:
        # Replace variable declarations
        modified_script = re.sub(
            rf'^\s*var\s+{var["name"]}\s*=\s*[^;]+;\s*(?://.*)?$',
            '',
            modified_script,
            flags=re.MULTILINE
        )

        # Replace variable usages (but not in comments or strings)
        # Use word boundaries to avoid partial replacements
        modified_script = re.sub(
            rf'\b{var["name"]}\b',
            var['new_name'],
            modified_script
        )

    # Remove the original function call at the end if it exists
    modified_script = re.sub(
        rf'^\s*{update_func_name}\s*\(\s*\)\s*;?\s*$',
        '',
        modified_script,
        flags=re.MULTILINE
    )

    # Clean up extra blank lines
    modified_script = re.sub(r'\n\n\n+', '\n\n', modified_script)
    modified_script = modified_script.strip()

    # Build putValue function
    putvalue_cases = []
    for var in variables:
        converter = 'Number' if var['type'] == '_pn_' else ('String' if var['type'] == '_ps_' else 'Boolean')
        default_val = '0' if var['type'] == '_pn_' else ('""' if var['type'] == '_ps_' else 'false')

        putvalue_cases.append(f"  if (id === '{var['new_name']}') {{")
        putvalue_cases.append(f"    {var['new_name']} = {converter}(value) || {default_val};")
        putvalue_cases.append(f"    update();")
        putvalue_cases.append(f"  }}")

    putvalue_body = ' else '.join(putvalue_cases)

    # Check if there's an init-like function or just rename the update function
    init_function = f"""function init() {{
  update();
}}"""

    # Rename the main update function to 'update' if it has a different name
    if update_func_name != 'update' and update_func_name in modified_script:
        modified_script = re.sub(
            rf'\bfunction\s+{update_func_name}\s*\(',
            'function update(',
            modified_script
        )
        # Also replace calls to the old function name
        modified_script = re.sub(
            rf'\b{update_func_name}\s*\(',
            'update(',
            modified_script
        )

    # Build final script
    new_script = f"""  <script><![CDATA[
{export_section}

{modified_script.strip()}

function putValue(id, value) {{
  {putvalue_body}
}}

init();
]]></script>"""

    # Replace the old script with new script
    new_content = re.sub(
        script_pattern,
        new_script,
        content,
        flags=re.DOTALL
    )

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓  Converted: {file_path.name}")
    return True

def main():
    """Main conversion process"""
    base_path = Path('/Users/jessecox/Documents/GitHub/wbg_widgets')

    folders = [
        'primitives',
        'hvac',
        'systems',
        'zones',
        'utilities',
        'controls',
        'indicators',
        'tanks',
        'safety',
        'specialty'
    ]

    total_converted = 0
    total_files = 0

    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            continue

        svg_files = list(folder_path.glob('*.svg'))
        print(f"\n{folder}/ ({len(svg_files)} files)")

        for svg_file in sorted(svg_files):
            total_files += 1
            if convert_svg_to_fuxa(svg_file):
                total_converted += 1

    print(f"\n{'='*50}")
    print(f"Conversion complete!")
    print(f"Total files processed: {total_files}")
    print(f"Files converted: {total_converted}")
    print(f"Files already converted: {total_files - total_converted}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
