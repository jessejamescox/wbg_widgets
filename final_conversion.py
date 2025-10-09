#!/usr/bin/env python3
"""
Final comprehensive conversion and fixes for all SVG widgets.
"""

import re
from pathlib import Path

def convert_complex_widgets(file_path):
    """Convert complex widgets that use getValue/setValue pattern"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already uses FUXA format
    if '//!export-start' in content or 'getValue' in content:
        return False, "Already in proper format"

    # Check if it has a script with vars to convert
    if '<script type="text/javascript">' not in content and '<script><![CDATA[' not in content:
        return False, "No script found"

    # Convert to 100% width/height on SVG tag
    svg_pattern = r'(<svg[^>]*?)\swidth=["\'][^"\']*["\']([^>]*?)\sheight=["\'][^"\']*["\']'
    content = re.sub(svg_pattern, r'\1 width="100%"\2 height="100%"', content, count=1)

    # Fix script tag format
    content = re.sub(r'<script type="text/javascript">\s*<!\[CDATA\[', '<script><![CDATA[', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, "Fixed"

def add_init_function(file_path):
    """Add missing init() function and DOM variable declarations"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'function init()' in content:
        return False, "Already has init()"

    # Extract script content
    script_pattern = r'<script><!\[CDATA\[(.*?)\]\]></script>'
    script_match = re.search(script_pattern, content, re.DOTALL)

    if not script_match:
        return False, "No script"

    script_content = script_match.group(1)

    # Check if there's an update function that uses DOM elements
    dom_refs = re.findall(r'document\.getElementById\([\'"]([^\'\"]+)[\'"]\)', script_content)

    if not dom_refs:
        return False, "No DOM refs"

    # Check if those DOM refs are used as variables (like _pn_valueText.textContent)
    needs_locals = False
    local_vars = set()

    for ref in set(dom_refs):
        # Convert to potential variable name
        var_name = '_pn_' + ref[0].lower() + ref[1:] if ref else ''
        var_name = ref.replace('-', '_')

        if var_name + '.' in script_content or var_name + '.textContent' in script_content:
            needs_locals = True
            local_vars.add((ref, var_name))

    if not needs_locals:
        return False, "No local vars needed"

    # Add local variable declarations at the start of update() function
    update_pattern = r'(function update\(\)\s*\{)'

    local_declarations = '\n  '.join([f"var {var} = document.getElementById('{dom_id}');"
                                       for dom_id, var in sorted(local_vars)])

    replacement = f"\\1\n  {local_declarations}\n"

    script_content = re.sub(update_pattern, replacement, script_content)

    # Replace in content
    new_script = f'<script><![CDATA[\n{script_content}\n]]></script>'
    new_content = re.sub(script_pattern, new_script, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, f"Added {len(local_vars)} local vars"

def main():
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

    print("\n=== Converting complex widgets ===")
    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            continue

        svg_files = list(folder_path.glob('*.svg'))

        for svg_file in sorted(svg_files):
            success, msg = convert_complex_widgets(svg_file)
            if success:
                print(f"✓ {svg_file.name}: {msg}")

    print("\n=== Adding local variable declarations ===")
    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            continue

        svg_files = list(folder_path.glob('*.svg'))

        for svg_file in sorted(svg_files):
            success, msg = add_init_function(svg_file)
            if success:
                print(f"✓ {svg_file.name}: {msg}")

    print("\n=== Final Stats ===")
    total_files = sum(len(list((base_path / folder).glob('*.svg')))
                      for folder in folders if (base_path / folder).exists())

    fuxa_files = 0
    percent_files = 0

    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            continue

        for svg_file in folder_path.glob('*.svg'):
            with open(svg_file, 'r') as f:
                content = f.read()
                if '//!export-start' in content or 'getValue' in content:
                    fuxa_files += 1
                if 'width="100%" height="100%"' in content[:200]:
                    percent_files += 1

    print(f"Total files: {total_files}")
    print(f"Files with FUXA format: {fuxa_files}")
    print(f"Files with 100% dimensions: {percent_files}")

if __name__ == '__main__':
    main()
