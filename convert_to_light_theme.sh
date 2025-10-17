#!/bin/bash

# Batch Light Theme Converter for WBG Widgets
# Converts all remaining SVG widgets from dark to light theme

echo "🎨 Starting batch light theme conversion..."

# Color mapping arrays
declare -A DARK_TO_LIGHT=(
  # Backgrounds
  ["#1a1a2e"]="#f5f7fa"
  ["#2c3e50"]="#ffffff"
  ["#34495e"]="#f5f7fa"
  ["#1a252f"]="#e0e0e0"

  # Text colors
  ["#ecf0f1"]="#2c3e50"
  ["#bdc3c7"]="#546e7a"
  ["#95a5a6"]="#78909c"
  ["#3498db"]="#1976d2"
  ["#00ff88"]="#1976d2"
  ["#00d4ff"]="#1976d2"

  # Component colors
  ["#546e7a"]="#eceff1"
  ["#455a64"]="#eceff1"
  ["#37474f"]="#cfd8dc"
  ["#263238"]="#cfd8dc"
  ["#78909c"]="#cfd8dc"
  ["#607d8b"]="#b0bec5"

  # Borders/Strokes
  ["#34495e"]="#90a4ae"
  ["#2c3e50"]="#90a4ae"
  ["#1a252f"]="#cfd8dc"

  # Accent blues
  ["#4a90e2"]="#2196f3"
  ["#5dade2"]="#64b5f6"
  ["#2874a6"]="#1976d2"

  # Data boxes
  ["#0a0e27"]="#263238"
  ["#1e3a5f"]="#546e7a"

  # Grays
  ["#7f8c8d"]="#b0bec5"
  ["#90a4ae"]="#90a4ae"
)

# Function to convert a single SVG file
convert_svg() {
  local file=$1
  local temp_file="${file}.tmp"

  echo "  Converting: $(basename $file)"

  cp "$file" "$temp_file"

  # Apply all color replacements
  for dark in "${!DARK_TO_LIGHT[@]}"; do
    light="${DARK_TO_LIGHT[$dark]}"
    # Case-insensitive replacement
    sed -i '' "s/${dark}/${light}/gI" "$temp_file"
  done

  # Adjust shadow opacities (reduce for light theme)
  sed -i '' 's/slope="0.25"/slope="0.12"/g' "$temp_file"
  sed -i '' 's/slope="0.3"/slope="0.15"/g' "$temp_file"
  sed -i '' 's/slope="0.35"/slope="0.15"/g' "$temp_file"

  # Adjust white highlights (increase for light theme)
  sed -i '' 's/rgba(255,255,255,0.08)/rgba(255,255,255,0.5)/g' "$temp_file"
  sed -i '' 's/rgba(255,255,255,0.1)/rgba(255,255,255,0.5)/g' "$temp_file"

  # Move temp file to original
  mv "$temp_file" "$file"
}

# Convert primitives (excluding already done ones)
echo ""
echo "📦 Phase 1: Converting Primitives..."
cd primitives/

for file in pump.svg pump-vfd.svg valve-*.svg damper*.svg sensor-*.svg \
            alarm-chip.svg filter.svg heater.svg coil-*.svg compressor.svg motor.svg; do
  if [ -f "$file" ]; then
    convert_svg "$file"
  fi
done

cd ..

# Convert HVAC widgets
echo ""
echo "🏭 Phase 2: Converting HVAC Widgets..."
cd hvac/

for file in ahu-*.svg fcu.svg rtu.svg vav.svg vav-reheat.svg \
            exhaust-fan.svg heat-exchanger.svg humidifier.svg \
            dehumidifier.svg economizer.svg; do
  if [ -f "$file" ]; then
    convert_svg "$file"
  fi
done

cd ..

# Convert utilities
echo ""
echo "⚡ Phase 3: Converting Utility Widgets..."
cd utilities/

for file in electrical-meter.svg water-meter.svg gas-meter.svg btu-meter.svg \
            switch-breaker.svg transformer.svg generator.svg ups.svg; do
  if [ -f "$file" ]; then
    convert_svg "$file"
  fi
done

cd ..

echo ""
echo "✅ Batch conversion complete!"
echo "📊 All widgets converted to light theme"
echo ""
echo "Next steps:"
echo "1. Review converted widgets"
echo "2. Test in FUXA"
echo "3. Adjust any specific colors if needed"
