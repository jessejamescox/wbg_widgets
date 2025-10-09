#!/usr/bin/env python3
"""
Final cleanup - remove duplicate variable declarations
"""
import re
from pathlib import Path

def final_cleanup(filepath):
    """Remove duplicate variable declarations after export section"""
    with open(filepath, 'r') as f:
        content = f.read()

    if '//!export-start' not in content:
        return False

    # Find the script section
    script_match = re.search(r'<script><!\[CDATA\[(.*?)\]\]></script>', content, re.DOTALL)
    if not script_match:
        return False

    script = script_match.group(1)

    # Find export section
    export_match = re.search(r'(//!export-start.*?//!export-end)', script, re.DOTALL)
    if not export_match:
        return False

    export_section = export_match.group(1)

    # Extract variable names from export section
    var_names = set()
    for line in export_section.split('\n'):
        match = re.match(r'\s*let\s+(_p[nbs]_\w+)', line)
        if match:
            var_names.add(match.group(1))

    if not var_names:
        return False

    # Find init function
    init_match = re.search(r'function init\(\)', script)
    if not init_match:
        return False

    # Get section between export-end and init
    export_end = export_match.end()
    init_start = init_match.start()
    between = script[export_end:init_start]

    # Remove duplicate declarations
    new_between_lines = []
    for line in between.split('\n'):
        # Skip lines that are duplicate variable declarations
        is_dup = False
        for var in var_names:
            if re.match(r'\s*let\s+' + re.escape(var) + r'\s*=', line):
                is_dup = True
                break

        if not is_dup:
            new_between_lines.append(line)

    new_between = '\n'.join(new_between_lines)

    # Rebuild script
    new_script = script[:export_end] + new_between + script[init_start:]

    # Rebuild content
    new_content = re.sub(
        r'<script><!\[CDATA\[.*?\]\]></script>',
        f'<script><![CDATA[\n{new_script}\n]]></script>',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w') as f:
        f.write(new_content)

    return True

def main():
    base_dirs = ['primitives', 'hvac', 'systems', 'zones', 'utilities',
                 'controls', 'indicators', 'tanks', 'safety', 'specialty']

    cleaned = 0
    for base_dir in base_dirs:
        for svg_file in sorted(Path(base_dir).glob('*.svg')):
            try:
                if final_cleanup(svg_file):
                    cleaned += 1
                    print(f"✓ {svg_file}")
            except Exception as e:
                print(f"✗ {svg_file}: {e}")

    print(f"\nCleaned {cleaned} files")

if __name__ == '__main__':
    main()
