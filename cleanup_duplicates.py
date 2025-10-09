#!/usr/bin/env python3
"""
Remove duplicate variable declarations after export section
"""
import re
from pathlib import Path

def clean_duplicates(filepath):
    """Remove duplicate variable declarations"""
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if no export section
    if '//!export-start' not in content:
        return False

    # Extract script section
    script_match = re.search(
        r'<script><!\[CDATA\[(.*?)\]\]></script>',
        content,
        re.DOTALL
    )

    if not script_match:
        return False

    script_content = script_match.group(1)

    # Extract export section
    export_match = re.search(
        r'//!export-start(.*?)//!export-end',
        script_content,
        re.DOTALL
    )

    if not export_match:
        return False

    export_section = export_match.group(1)

    # Get all exported variable names
    export_vars = set()
    for line in export_section.split('\n'):
        match = re.match(r'\s*let\s+(_p[nbs]_\w+)', line)
        if match:
            export_vars.add(match.group(1))

    if not export_vars:
        return False

    # Find init function location
    init_match = re.search(r'function init\(\)', script_content)
    if not init_match:
        return False

    init_pos = init_match.start()

    # Get section after export-end and before init()
    export_end_match = re.search(r'//!export-end', script_content)
    between_section = script_content[export_end_match.end():init_pos]

    # Remove duplicate variable declarations
    new_between = ""
    for line in between_section.split('\n'):
        # Skip lines that declare exported variables
        skip = False
        for var in export_vars:
            if re.match(r'\s*let\s+' + var + r'\s*=', line):
                skip = True
                break

        if not skip:
            new_between += line + '\n'

    # Rebuild script
    new_script = (
        script_content[:export_end_match.end()] +
        new_between +
        script_content[init_pos:]
    )

    # Replace in content
    new_content = re.sub(
        r'<script><!\[CDATA\[.*?\]\]></script>',
        f'<script><![CDATA[\n{new_script}\n]]></script>',
        content,
        flags=re.DOTALL
    )

    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)

    return True

def main():
    base_dirs = ['primitives', 'hvac', 'systems', 'zones', 'utilities',
                 'controls', 'indicators', 'tanks', 'safety', 'specialty']

    cleaned_count = 0

    for base_dir in base_dirs:
        svg_files = list(Path(base_dir).glob('*.svg'))

        for filepath in sorted(svg_files):
            try:
                if clean_duplicates(filepath):
                    cleaned_count += 1
                    print(f"✓ Cleaned {filepath}")
            except Exception as e:
                print(f"✗ Error cleaning {filepath}: {e}")

    print(f"\nCleaned {cleaned_count} files")

if __name__ == '__main__':
    main()
