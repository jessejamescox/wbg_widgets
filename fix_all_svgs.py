#!/usr/bin/env python3
"""
Fix all SVG files that were improperly converted.
This script will:
1. Fix width/height on SVG root only (not internal elements)
2. Properly convert scripts to FUXA format
3. Fix the putValue function
4. Remove DOM element references from exports
"""

import os
import re
from pathlib import Path

def fix_svg_file(file_path):
    """Fix a single SVG file"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Step 1: Fix width/height on SVG root element only
    # First, restore any broken width/height in rect elements (revert 100% back to numbers where inappropriate)
    # We'll do this by reading the original file if it exists in git

    # Step 2: Fix the SVG root element width/height
    # Match only the opening SVG tag
    svg_pattern = r'(<svg[^>]*?)\swidth=["\'][^"\']*["\']([^>]*?)\sheight=["\'][^"\']*["\']'
    content = re.sub(svg_pattern, r'\1 width="100%"\2 height="100%"', content, count=1)

    # Step 3: Check if file needs fixing
    if '//!export-start' not in content:
        return False, "No export section found"

    # Check if putValue is broken (contains "else" incorrectly)
    if 'if (id ===' in content and '{ else ' in content:
        # Need to fix putValue
        pass
    else:
        return False, "Already properly formatted"

    # Extract the script content
    script_pattern = r'<script><!\[CDATA\[(.*?)\]\]></script>'
    script_match = re.search(script_pattern, content, re.DOTALL)

    if not script_match:
        return False, "No script found"

    script_content = script_match.group(1)

    # Extract export section
    export_pattern = r'//!export-start(.*?)//!export-end'
    export_match = re.search(export_pattern, script_content, re.DOTALL)

    if not export_match:
        return False, "No export section"

    export_section = export_match.group(0)

    # Parse exported variables (excluding DOM element references)
    export_vars = []
    for line in export_match.group(1).strip().split('\n'):
        line = line.strip()
        if not line or '//' in line[:2]:
            continue

        # Match: let _pn_varname = value;
        var_match = re.match(r'let\s+(_p[nsb]_\w+)\s*=\s*(.+?);', line)
        if var_match:
            var_name = var_match.group(1)
            var_value = var_match.group(2)

            # Skip DOM element references
            if 'document.getElementById' in var_value or 'document.querySelector' in var_value:
                continue

            # Determine type from prefix
            if var_name.startswith('_pn_'):
                var_type = 'number'
            elif var_name.startswith('_ps_'):
                var_type = 'string'
            elif var_name.startswith('_pb_'):
                var_type = 'boolean'
            else:
                continue

            export_vars.append({
                'name': var_name,
                'type': var_type,
                'value': var_value
            })

    if not export_vars:
        return False, "No valid export variables"

    # Remove DOM references from export section
    cleaned_export_lines = ['//!export-start']
    for line in export_match.group(1).strip().split('\n'):
        line_stripped = line.strip()
        if line_stripped and 'document.getElementById' not in line_stripped and 'document.querySelector' not in line_stripped:
            cleaned_export_lines.append(line.rstrip())
    cleaned_export_lines.append('//!export-end')
    cleaned_export = '\n'.join(cleaned_export_lines)

    # Build proper putValue function
    putvalue_cases = []
    for var in export_vars:
        if var['type'] == 'number':
            converter = 'Number'
            default = '0'
        elif var['type'] == 'string':
            converter = 'String'
            default = '""'
        else:  # boolean
            converter = 'Boolean'
            default = 'false'

        putvalue_cases.append(f"  if (id === '{var['name']}') {{")
        putvalue_cases.append(f"    {var['name']} = {converter}(value) || {default};")
        putvalue_cases.append(f"    update();")
        putvalue_cases.append(f"  }} else ")

    # Remove the trailing " else " from the last case
    if putvalue_cases:
        putvalue_cases[-1] = putvalue_cases[-1].rstrip(' else ')

    putvalue_function = 'function putValue(id, value) {\n' + '\n'.join(putvalue_cases) + '\n}'

    # Replace the broken putValue function
    putvalue_pattern = r'function putValue\(id, value\)\s*\{[^}]*?\}'
    script_content = re.sub(putvalue_pattern, putvalue_function, script_content, flags=re.DOTALL)

    # Replace the export section
    script_content = re.sub(export_pattern, cleaned_export, script_content, flags=re.DOTALL)

    # Ensure init() function exists
    if 'function init()' not in script_content:
        # Add init function before putValue
        init_func = '\nfunction init() {\n  update();\n}\n\n'
        script_content = re.sub(r'(function putValue)', init_func + r'\1', script_content)

    # Build new script tag
    new_script = f'  <script><![CDATA[\n{script_content.strip()}\n]]></script>'

    # Replace in content
    new_content = re.sub(script_pattern, new_script, content, flags=re.DOTALL)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "Fixed"

def main():
    """Main fix process"""
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

    total_fixed = 0
    total_files = 0

    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            continue

        svg_files = list(folder_path.glob('*.svg'))
        print(f"\n{folder}/ ({len(svg_files)} files)")

        for svg_file in sorted(svg_files):
            total_files += 1
            success, msg = fix_svg_file(svg_file)
            if success:
                print(f"  ✓  {svg_file.name}: {msg}")
                total_fixed += 1
            else:
                print(f"  -  {svg_file.name}: {msg}")

    print(f"\n{'='*50}")
    print(f"Fix complete!")
    print(f"Total files processed: {total_files}")
    print(f"Files fixed: {total_fixed}")
    print(f"{'='*50}")

if __name__ == '__main__':
    main()
