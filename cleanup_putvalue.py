#!/usr/bin/env python3
"""
Clean up the malformed putValue functions that have duplicate code.
"""

import re
from pathlib import Path

def cleanup_file(file_path):
    """Remove the malformed duplicate putValue code"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the putValue function and remove everything after the first closing brace
    # Pattern: match from "function putValue" to first complete closing brace, then remove garbage
    pattern = r'(function putValue\(id, value\)\s*\{(?:[^{}]|\{[^{}]*\})*\})\s*\}\s*else\s+if\s+\(id\s+===.*?(?=\n\s*init\(\);)'

    cleaned = re.sub(pattern, r'\1', content, flags=re.DOTALL)

    if cleaned != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        return True
    return False

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

    total_fixed = 0
    for folder in folders:
        folder_path = base_path / folder
        if not folder_path.exists():
            continue

        svg_files = list(folder_path.glob('*.svg'))

        for svg_file in svg_files:
            if cleanup_file(svg_file):
                print(f"✓ Cleaned: {svg_file}")
                total_fixed += 1

    print(f"\nTotal files cleaned: {total_fixed}")

if __name__ == '__main__':
    main()
