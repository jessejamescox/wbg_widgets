#!/bin/bash

echo "🔍 Fixing text and overlay visibility for light theme..."

fix_file() {
  local file=$1
  echo "  Fixing: $(basename $file)"
  
  # Fix text colors - ensure dark text on light backgrounds
  # Make sure fill colors are dark enough to be visible
  sed -i '' 's/fill:#ecf0f1/fill:#2c3e50/g' "$file"
  sed -i '' 's/fill:#bdc3c7/fill:#546e7a/g' "$file"
  sed -i '' 's/fill:#95a5a6/fill:#546e7a/g' "$file"
  sed -i '' 's/fill:#7f8c8d/fill:#546e7a/g' "$file"
  
  # Fix any remaining light text colors
  sed -i '' 's/fill: #ecf0f1/fill: #2c3e50/g' "$file"
  sed -i '' 's/fill: #bdc3c7/fill: #546e7a/g' "$file"
  sed -i '' 's/fill: #95a5a6/fill: #546e7a/g' "$file"
  sed -i '' 's/fill: #7f8c8d/fill: #546e7a/g' "$file"
  
  # Ensure label text is dark
  sed -i '' 's/\(class="[^"]*label[^"]*"[^>]*\)fill="#[^"]*"/\1fill="#546e7a"/g' "$file"
  
  # Ensure value text is visible blue
  sed -i '' 's/\(class="[^"]*value[^"]*"[^>]*\)fill="#3498db"/\1fill="#1976d2"/g' "$file"
  
  # Make sure any white or light overlays are removed or darkened
  sed -i '' 's/fill="white"/fill="#2c3e50"/g' "$file"
  sed -i '' 's/fill="#fff"/fill="#2c3e50"/g' "$file"
  sed -i '' 's/fill="#ffffff"/fill="#2c3e50"/g' "$file"
  
  # Fix stroke colors for visibility
  sed -i '' 's/stroke:#ecf0f1/stroke:#90a4ae/g' "$file"
  sed -i '' 's/stroke: #ecf0f1/stroke: #90a4ae/g' "$file"
}

# Fix all primitives
echo ""
echo "📦 Fixing Primitives..."
cd primitives
for file in *.svg; do
  if [ -f "$file" ]; then
    fix_file "$file"
  fi
done
cd ..

# Fix all HVAC
echo ""
echo "🏭 Fixing HVAC Widgets..."
cd hvac
for file in *.svg; do
  if [ -f "$file" ]; then
    fix_file "$file"
  fi
done
cd ..

# Fix all utilities
echo ""
echo "⚡ Fixing Utilities..."
cd utilities
for file in *.svg; do
  if [ -f "$file" ]; then
    fix_file "$file"
  fi
done
cd ..

echo ""
echo "✅ Text visibility fixes complete!"
