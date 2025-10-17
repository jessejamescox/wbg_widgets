#!/usr/bin/env python3
"""
Batch Light Theme Converter for WBG Widgets
Converts all SVG widgets from dark to light theme
"""

import os
import re
from pathlib import Path

# Color mapping: Dark -> Light
COLOR_MAP = {
    # Backgrounds
    '#1a1a2e': '#f5f7fa',
    '#2c3e50': '#ffffff',
    '#34495e': '#f5f7fa',
    '#1a252f': '#e0e0e0',

    # Text colors
    '#ecf0f1': '#2c3e50',
    '#bdc3c7': '#546e7a',
    '#95a5a6': '#78909c',
    '#3498db': '#1976d2',
    '#00ff88': '#1976d2',
    '#00d4ff': '#1976d2',
    '#7f8c8d': '#78909c',

    # Component colors
    '#546e7a': '#eceff1',
    '#455a64': '#eceff1',
    '#37474f': '#cfd8dc',
    '#263238': '#cfd8dc',
    '#78909c': '#cfd8dc',
    '#607d8b': '#b0bec5',
    '#90a4ae': '#90a4ae',  # Keep this
    '#b0bec5': '#b0bec5',  # Keep this

    # Accent blues
    '#4a90e2': '#2196f3',
    '#5dade2': '#64b5f6',
    '#2874a6': '#1976d2',

    # Data displays
    '#0a0e27': '#263238',
    '#1e3a5f': '#546e7a',

    # Additional mappings
    '#4a5568': '#cfd8dc',
    '#2d3748': '#b0bec5',
    '#1a202c': '#90a4ae',
}

def convert_svg_file(file_path):
    """Convert a single SVG file to light theme"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace colors (case-insensitive)
        for dark_color, light_color in COLOR_MAP.items():
            # Replace both lowercase and uppercase versions
            content = re.sub(dark_color, light_color, content, flags=re.IGNORECASE)

        # Adjust shadow opacities (reduce for light theme)
        content = re.sub(r'slope="0\.25"', 'slope="0.12"', content)
        content = re.sub(r'slope="0\.3"', 'slope="0.15"', content)
        content = re.sub(r'slope="0\.35"', 'slope="0.15"', content)

        # Adjust white highlights (increase for light theme)
        content = re.sub(r'rgba\(255,255,255,0\.08\)', 'rgba(255,255,255,0.5)', content)
        content = re.sub(r'rgba\(255,255,255,0\.1\)', 'rgba(255,255,255,0.5)', content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"  ❌ Error converting {file_path.name}: {e}")
        return False

def main():
    print("🎨 Starting batch light theme conversion...\n")

    base_dir = Path('.')
    total_converted = 0

    # Phase 1: Primitives
    print("📦 Phase 1: Converting Primitives...")
    primitives_dir = base_dir / 'primitives'
    primitive_files = [
        'pump.svg', 'pump-vfd.svg',
        'valve-2pos.svg', 'valve-analog.svg', 'valve-3way.svg',
        'damper.svg', 'damper-2pos.svg',
        'sensor-chip-temp.svg', 'sensor-chip-humidity.svg',
        'sensor-chip-pressure.svg', 'sensor-chip-co2.svg',
        'alarm-chip.svg', 'filter.svg', 'heater.svg',
        'coil-heating.svg', 'coil-cooling.svg',
        'compressor.svg', 'motor.svg'
    ]

    for filename in primitive_files:
        file_path = primitives_dir / filename
        if file_path.exists():
            if convert_svg_file(file_path):
                print(f"  ✓ {filename}")
                total_converted += 1

    # Phase 2: HVAC
    print("\n🏭 Phase 2: Converting HVAC Widgets...")
    hvac_dir = base_dir / 'hvac'
    hvac_files = [
        'ahu-compact.svg', 'ahu-detailed.svg',
        'fcu.svg', 'rtu.svg', 'vav.svg', 'vav-reheat.svg',
        'exhaust-fan.svg', 'heat-exchanger.svg',
        'humidifier.svg', 'dehumidifier.svg', 'economizer.svg'
    ]

    for filename in hvac_files:
        file_path = hvac_dir / filename
        if file_path.exists():
            if convert_svg_file(file_path):
                print(f"  ✓ {filename}")
                total_converted += 1

    # Phase 3: Utilities
    print("\n⚡ Phase 3: Converting Utility Widgets...")
    utilities_dir = base_dir / 'utilities'
    utility_files = [
        'electrical-meter.svg', 'water-meter.svg', 'gas-meter.svg', 'btu-meter.svg',
        'switch-breaker.svg', 'transformer.svg', 'generator.svg', 'ups.svg'
    ]

    for filename in utility_files:
        file_path = utilities_dir / filename
        if file_path.exists():
            if convert_svg_file(file_path):
                print(f"  ✓ {filename}")
                total_converted += 1

    # Also convert the enhanced samples that weren't done yet
    print("\n✨ Converting Enhanced Samples...")
    enhanced_files = [
        ('utilities/power-meter-enhanced.svg', 'power-meter-enhanced.svg'),
        ('utilities/bess.svg', 'bess.svg'),
    ]

    for file_path_str, filename in enhanced_files:
        file_path = base_dir / file_path_str
        if file_path.exists():
            if convert_svg_file(file_path):
                print(f"  ✓ {filename}")
                total_converted += 1

    print(f"\n✅ Batch conversion complete!")
    print(f"📊 {total_converted} widgets converted to light theme\n")
    print("Next steps:")
    print("1. Review converted widgets in browser/FUXA")
    print("2. Test functionality")
    print("3. Fine-tune any specific colors if needed")

if __name__ == '__main__':
    main()
