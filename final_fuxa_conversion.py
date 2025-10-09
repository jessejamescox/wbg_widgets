#!/usr/bin/env python3
"""
Final FUXA conversion script - properly handles all edge cases
"""
import re
import os
from pathlib import Path

def extract_variables(script_content):
    """Extract variables that should be exported to FUXA"""
    variables = []

    # Pattern to match var declarations
    var_pattern = r'^\s*var\s+(\w+)\s*=\s*(.+?);'

    # Variables to skip (these are internal/local)
    skip_vars = {
        'rotation', 'animationId', 'svg', 'intervalId', 'currentAngle',
        'blades', 'motor', 'coil', 'fan', 'pump', 'damper', 'valve',
        'statusText', 'valueText', 'indicator', 'gaugeFill', 'stem',
        'stemTop', 'posIndicator', 'commandIndicator', 'feedbackIndicator',
        'tempText', 'humidText', 'co2Text', 'pressText',
        'powerLed', 'alarmLed', 'troubleLed', 'silencedLed',
        'mainStatusText', 'troubleText', 'troubleDetail',
        'silenceButton', 'resetButton', 'testButton',
        'statusLed', 'alarmRing', 'batteryFill', 'batteryText',
        'damperBlade', 'bladeGroup', 'fusibleLink', 'airflowIndicators',
        'positionText', 'linkText', 'alarmLight'
    }

    for line in script_content.split('\n'):
        # Skip lines with document.getElementById
        if 'document.getElementById' in line or 'document.currentScript' in line:
            continue

        match = re.match(var_pattern, line)
        if match:
            var_name = match.group(1)
            var_value = match.group(2).strip()

            # Skip internal variables
            if var_name in skip_vars:
                continue

            # Determine variable type and prefix
            if var_value.lower() in ['true', 'false']:
                var_type = '_pb_'
                variables.append((var_name, var_type, var_value))
            elif var_value.startswith('"') or var_value.startswith("'"):
                var_type = '_ps_'
                variables.append((var_name, var_type, var_value))
            elif re.match(r'^-?\d+\.?\d*$', var_value):
                var_type = '_pn_'
                variables.append((var_name, var_type, var_value))

    return variables

def convert_script(script_content, variables):
    """Convert script to FUXA format"""

    # Build export section
    export_section = "//!export-start\n"
    for var_name, var_type, var_value in variables:
        export_section += f"let {var_type}{var_name} = {var_value};\n"
    export_section += "//!export-end\n\n"

    # Replace var declarations with let for local variables
    new_script = script_content

    # Replace exported variable references
    for var_name, var_type, _ in variables:
        # Replace variable usage (but be careful with partial matches)
        new_script = re.sub(
            r'\b' + var_name + r'\b',
            var_type + var_name,
            new_script
        )

    # Replace var declarations with let for local variables
    new_script = re.sub(r'^\s*var\s+(\w+)', r'let \1', new_script, flags=re.MULTILINE)

    # Remove old var declarations for exported variables
    for var_name, var_type, _ in variables:
        new_script = re.sub(
            r'^\s*let\s+' + var_type + var_name + r'\s*=\s*.+?;\s*$',
            '',
            new_script,
            flags=re.MULTILINE
        )

    # Find the main function (updateWidget or similar)
    update_func_match = re.search(r'function\s+(updateWidget|update)\s*\(\s*\)\s*\{', new_script)

    if update_func_match:
        update_func_name = update_func_match.group(1)
    else:
        update_func_name = 'update'

    # Build init function
    init_func = f"""function init() {{
  update();
}}

"""

    # Build putValue function
    putvalue_func = "function putValue(id, value) {\n"

    for i, (var_name, var_type, _) in enumerate(variables):
        if i == 0:
            putvalue_func += f"  if (id === '{var_type}{var_name}') {{\n"
        else:
            putvalue_func += f"  }} else if (id === '{var_type}{var_name}') {{\n"

        if var_type == '_pn_':
            putvalue_func += f"    {var_type}{var_name} = Number(value) || 0;\n"
        elif var_type == '_ps_':
            putvalue_func += f"    {var_type}{var_name} = String(value) || \"\";\n"
        elif var_type == '_pb_':
            putvalue_func += f"    {var_type}{var_name} = !!value;\n"

        putvalue_func += f"    update();\n"

    if variables:
        putvalue_func += "  }\n"
    putvalue_func += "}\n\n"

    # Rename updateWidget to update if needed
    if update_func_name == 'updateWidget':
        new_script = new_script.replace('function updateWidget()', 'function update()')
        new_script = new_script.replace('updateWidget()', 'update()')

    # Remove the final function call (updateWidget() or update())
    new_script = re.sub(r'\n\s*update\(\);?\s*$', '', new_script)
    new_script = re.sub(r'\n\s*updateWidget\(\);?\s*$', '', new_script)

    # Build final script
    if variables:
        final_script = export_section + init_func + new_script.strip() + "\n\n" + putvalue_func + "init();"
    else:
        # No variables to export, just add init
        final_script = init_func + new_script.strip() + "\n\ninit();"

    return final_script

def convert_svg_file(filepath):
    """Convert a single SVG file to FUXA format"""

    with open(filepath, 'r') as f:
        content = f.read()

    # Check if already converted
    if '//!export-start' in content:
        return False, "Already has FUXA export format"

    if 'svg.getValue = function' in content:
        return False, "Uses getValue/setValue format (alternative FUXA format)"

    # Update SVG element to use responsive sizing
    content = re.sub(
        r'<svg([^>]*?)width="[^"]*"([^>]*?)height="[^"]*"',
        r'<svg\1width="100%"\2height="100%"',
        content,
        count=1  # Only replace the first occurrence (root SVG element)
    )

    # Extract script section
    script_match = re.search(
        r'<script[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</script>',
        content,
        re.DOTALL
    )

    if not script_match:
        return False, "No script section found"

    script_content = script_match.group(1)

    # Extract variables
    variables = extract_variables(script_content)

    # Convert script
    new_script = convert_script(script_content, variables)

    # Replace script in content
    new_content = re.sub(
        r'<script[^>]*>\s*<!\[CDATA\[.*?\]\]>\s*</script>',
        f'<script><![CDATA[\n{new_script}\n]]></script>',
        content,
        flags=re.DOTALL
    )

    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)

    return True, f"Converted with {len(variables)} exported variables"

def main():
    """Main conversion process"""

    base_dirs = ['primitives', 'hvac', 'systems', 'zones', 'utilities',
                 'controls', 'indicators', 'tanks', 'safety', 'specialty']

    converted_count = 0
    skipped_count = 0
    error_count = 0

    results = []

    for base_dir in base_dirs:
        svg_files = list(Path(base_dir).glob('*.svg'))

        for filepath in sorted(svg_files):
            try:
                success, message = convert_svg_file(filepath)

                if success:
                    converted_count += 1
                    results.append(f"✓ {filepath}: {message}")
                else:
                    skipped_count += 1
                    results.append(f"- {filepath}: {message}")
            except Exception as e:
                error_count += 1
                results.append(f"✗ {filepath}: ERROR - {str(e)}")

    # Print results
    print("\n" + "="*80)
    print("FUXA CONVERSION RESULTS")
    print("="*80 + "\n")

    for result in results:
        print(result)

    print("\n" + "="*80)
    print(f"SUMMARY: {converted_count} converted, {skipped_count} skipped, {error_count} errors")
    print("="*80)

if __name__ == '__main__':
    main()
