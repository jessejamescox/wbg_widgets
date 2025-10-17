# Light Theme Design Guide

## Overview

This guide provides the complete color palette and design specifications for converting all widgets to a professional light theme suitable for modern BMS/SCADA control rooms with ambient lighting.

## Light Theme Color Palette

### Background Colors
```css
--bg-primary: #f5f7fa;          /* Main background - light gray-blue */
--bg-secondary: #ffffff;         /* Cards and panels - white */
--bg-tertiary: #e8ecf1;          /* Alternate sections - lighter gray */
--bg-card: #ffffff;              /* Widget cards - white */
--bg-panel: #f5f7fa;             /* Data panels - light gray */
```

### Text Colors
```css
--text-primary: #2c3e50;         /* Primary text - dark charcoal */
--text-secondary: #546e7a;       /* Secondary text/labels - medium gray */
--text-tertiary: #78909c;        /* Tertiary text/units - light gray */
--text-value: #1976d2;           /* Values/data - deep blue */
```

### Component Colors
```css
/* Enclosures & Equipment */
--component-light: #eceff1;      /* Light metal/enclosure */
--component-medium: #cfd8dc;     /* Medium metal/enclosure */
--component-dark: #b0bec5;       /* Dark metal/enclosure */

/* Ductwork & Piping */
--duct-light: #eceff1;           /* Light duct */
--duct-medium: #cfd8dc;          /* Medium duct */
--duct-dark: #b0bec5;            /* Dark duct */

/* Borders & Strokes */
--border-primary: #90a4ae;       /* Primary borders */
--border-secondary: #cfd8dc;     /* Secondary borders */
--border-light: #e0e0e0;         /* Light borders */
```

### Status Colors (Universal - Same as Dark Theme)
```css
--status-ok: #27ae60;            /* Green - Normal/On */
--status-warning: #f39c12;       /* Orange - Warning/Caution */
--status-alarm: #e74c3c;         /* Red - Alarm/Stop/Emergency */
--status-inactive: #95a5a6;      /* Gray - Off/Disabled */
```

### Accent Colors
```css
--accent-blue: #2196f3;          /* Primary blue accent */
--accent-deep-blue: #1976d2;     /* Deep blue for values */
--accent-light-blue: #64b5f6;    /* Light blue for highlights */
--accent-cyan: #00bcd4;          /* Cyan for special indicators */
```

### Shadow & Effects
```css
--shadow-subtle: rgba(0,0,0,0.08);     /* Subtle shadows */
--shadow-medium: rgba(0,0,0,0.12);     /* Medium shadows */
--shadow-strong: rgba(0,0,0,0.15);     /* Strong shadows */
--highlight-white: rgba(255,255,255,0.5);  /* White highlights */
```

## Conversion Map: Dark → Light

### Direct Replacements

| Element | Dark Theme | Light Theme |
|---------|------------|-------------|
| **Backgrounds** |||
| Main BG | `#1a1a2e` | `#f5f7fa` |
| Card BG | `#2c3e50` | `#ffffff` |
| Panel BG | `#34495e` | `#f5f7fa` |
| Section BG | `#2c3e50` | `#f5f7fa` |
| **Text** |||
| Primary | `#ecf0f1` | `#2c3e50` |
| Secondary | `#bdc3c7` | `#546e7a` |
| Tertiary | `#95a5a6` | `#78909c` |
| Values | `#3498db` or `#00ff88` | `#1976d2` |
| **Components** |||
| Enclosure Start | `#546e7a` or `#455a64` | `#eceff1` |
| Enclosure End | `#37474f` or `#263238` | `#cfd8dc` |
| Duct Start | `#90a4ae` | `#eceff1` |
| Duct Mid | `#78909c` | `#cfd8dc` |
| Duct End | `#607d8b` | `#b0bec5` |
| **Borders** |||
| Primary | `#2c3e50` or `#34495e` | `#90a4ae` |
| Secondary | `#1a252f` | `#cfd8dc` |
| Light | N/A | `#e0e0e0` |
| **Shadows** |||
| Opacity | `0.25-0.3` | `0.08-0.15` |

### Gradient Conversions

#### Enclosures (Equipment Bodies)
```css
/* DARK */
linearGradient: #546e7a → #37474f
linearGradient: #455a64 → #263238

/* LIGHT */
linearGradient: #eceff1 → #cfd8dc
```

#### Ductwork/Piping
```css
/* DARK */
linearGradient: #90a4ae → #78909c → #607d8b

/* LIGHT */
linearGradient: #eceff1 → #cfd8dc → #b0bec5
```

#### Radial Gradients (Hubs, Buttons)
```css
/* DARK */
radialGradient: #546e7a (center) → #263238 (edge)

/* LIGHT */
radialGradient: #b0bec5 (center) → #78909c (edge)
```

## Widget-Specific Examples

### 1. Fan (Primitive)

**Dark Theme → Light Theme Changes:**

```css
/* Background Card */
fill: #2c3e50 opacity: 0.3  →  fill: #ffffff stroke: #e0e0e0

/* Housing Gradient */
#455a64 → #263238  →  #eceff1 → #cfd8dc

/* Blade Gradient */
#5dade2 → #3498db → #2874a6  →  #64b5f6 → #2196f3 → #1976d2

/* Hub Gradient */
#546e7a → #263238  →  #b0bec5 → #78909c

/* Text - Labels */
fill: #ecf0f1  →  fill: #546e7a

/* Text - Values */
fill: #3498db  →  fill: #1976d2

/* Shadow Opacity */
slope: 0.3  →  slope: 0.15
```

### 2. VAV Box (HVAC)

**Key Changes:**

```css
/* Background */
fill: #1a1a2e  →  fill: #f5f7fa

/* VAV Enclosure */
stroke: #2c3e50  →  stroke: #90a4ae
gradient: #546e7a → #37474f  →  #eceff1 → #cfd8dc

/* Ductwork */
stroke: #34495e  →  stroke: #90a4ae
gradient: #90a4ae → #78909c → #607d8b  →  #eceff1 → #cfd8dc → #b0bec5

/* Damper */
fill: #7f8c8d stroke: #2c3e50  →  fill: #b0bec5 stroke: #78909c

/* Airflow Particles */
fill: #5dade2  →  fill: #64b5f6

/* Data Panel BG */
fill: #34495e stroke: #2c3e50  →  fill: #ffffff stroke: #cfd8dc

/* Panel Sections */
fill: #2c3e50 stroke: #1a252f  →  fill: #f5f7fa stroke: #e0e0e0

/* Text Labels */
fill: #bdc3c7  →  fill: #546e7a

/* Text Values */
fill: #3498db  →  fill: #1976d2

/* Text Units */
fill: #95a5a6  →  fill: #78909c

/* Highlights */
rgba(255,255,255,0.08)  →  rgba(255,255,255,0.5)
```

### 3. Power Meter (Utility)

**Key Changes:**

```css
/* Meter Body Gradient */
#2c3e50 → #1a1a2e  →  #eceff1 → #cfd8dc

/* Bezel Gradient */
#4a5568 → #2d3748 → #1a202c  →  #cfd8dc → #b0bec5 → #90a4ae

/* Display Background */
fill: #0a0e27 stroke: #1e3a5f  →  fill: #263238 stroke: #546e7a

/* Text - Primary (LED style) */
fill: #00ff88 or #00d4ff  →  fill: #1976d2

/* Text - Labels */
fill: #7f8c8d  →  fill: #546e7a

/* Text - Sub-values */
fill: #3498db  →  fill: #1976d2

/* Data Boxes */
fill: #1a252f stroke: #2c3e50  →  fill: #f5f7fa stroke: #e0e0e0
```

### 4. BESS (Battery Storage)

**Key Changes:**

```css
/* Background */
fill: #1a1a2e  →  fill: #f5f7fa

/* Battery Container Gradient */
#455a64 → #263238  →  #eceff1 → #cfd8dc

/* Battery Cell Gradient */
#546e7a → #37474f → #263238  →  #eceff1 → #cfd8dc → #b0bec5

/* SOC Fill (Gradients - Keep same colors) */
Low: #e74c3c → #c0392b  (no change)
Medium: #f39c12 → #d68910  (no change)
High: #27ae60 → #229954  (no change)

/* Panel Background */
fill: #2c3e50 stroke: #34495e  →  fill: #ffffff stroke: #cfd8dc

/* Panel Header */
fill: #34495e  →  fill: #f5f7fa

/* Text - Labels */
fill: #95a5a6  →  fill: #546e7a

/* Text - Values */
fill: #3498db or #00ff88  →  fill: #1976d2

/* Flow Lines */
stroke: varies  →  (keep same - status colors)
```

## Step-by-Step Conversion Process

### For Each Widget:

1. **Update Background**
   - Main background: `#1a1a2e` → `#f5f7fa`
   - Card backgrounds: Dark → `#ffffff`
   - Panel backgrounds: Dark → `#f5f7fa`

2. **Update Gradients**
   - Enclosures: Dark grays → Light grays (`#eceff1` → `#cfd8dc`)
   - Ductwork: Dark metallics → Light metallics
   - Use conversion table above

3. **Update Text**
   - Labels: Light → Medium gray (`#546e7a`)
   - Values: Bright colors → Deep blue (`#1976d2`)
   - Units: Light gray → Medium gray (`#78909c`)

4. **Update Borders/Strokes**
   - Dark borders → Medium gray (`#90a4ae`)
   - Very dark → Light gray (`#cfd8dc`, `#e0e0e0`)

5. **Update Shadows**
   - Reduce opacity: `0.25-0.3` → `0.08-0.15`
   - Lighter, more subtle

6. **Update Highlights**
   - White overlays: `0.08-0.1` → `0.5-0.6` (brighter)

7. **Keep Status Colors Unchanged**
   - Green (#27ae60), Orange (#f39c12), Red (#e74c3c), Gray (#95a5a6)
   - These are universally recognized

## Typography Standards (Same as Dark Theme)

```css
/* Headers */
font-family: 'Segoe UI', Arial, sans-serif
font-size: 16-20px
font-weight: 700

/* Labels */
font-family: 'Segoe UI', Arial, sans-serif
font-size: 9-11px
font-weight: 600

/* Values */
font-family: 'Consolas', 'Courier New', monospace (or 'Orbitron' for digital displays)
font-size: 13-36px
font-weight: 700

/* Units */
font-family: 'Segoe UI', Arial, sans-serif
font-size: 9-13px
font-weight: 600
```

## Animation Standards (Same as Dark Theme)

All animations remain the same - only colors change:
- Rotation speeds
- Pulse timing
- Flow animations
- Alarm flash rates

## CSS Class Structure Template

```css
<style>
  /* Component Styles - Light Theme */
  .component-body { fill: url(#gradient); stroke: #90a4ae; stroke-width: 2; }
  .component-part { fill: #b0bec5; stroke: #78909c; }

  /* Text Styles */
  .label-text { fill: #546e7a; font-family: 'Segoe UI'; font-size: 10px; font-weight: 600; }
  .value-text { fill: #1976d2; font-family: 'Consolas', monospace; font-size: 14px; font-weight: 700; }
  .unit-text { fill: #78909c; font-family: 'Segoe UI'; font-size: 9px; }

  /* Status Indicators */
  .status-normal { fill: #27ae60; }
  .status-warning { fill: #f39c12; }
  .status-alarm { fill: #e74c3c; }
  .status-inactive { fill: #95a5a6; }

  /* Panels */
  .panel-bg { fill: #ffffff; stroke: #cfd8dc; stroke-width: 1.5; }
  .panel-section { fill: #f5f7fa; stroke: #e0e0e0; stroke-width: 1; }

  /* Animations - Same as dark theme */
  @keyframes pulse { 0%, 100% { opacity: 0.6; } 50% { opacity: 1; } }
</style>
```

## Gradient Template

```xml
<!-- Light Theme Gradients -->

<!-- Enclosure/Equipment Body -->
<linearGradient id="enclosureGradient" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#eceff1;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#cfd8dc;stop-opacity:1" />
</linearGradient>

<!-- Ductwork/Piping -->
<linearGradient id="ductGradient" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" style="stop-color:#eceff1;stop-opacity:1" />
  <stop offset="50%" style="stop-color:#cfd8dc;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#b0bec5;stop-opacity:1" />
</linearGradient>

<!-- Hub/Button (Radial) -->
<radialGradient id="hubGradient" cx="50%" cy="50%" r="50%">
  <stop offset="0%" style="stop-color:#b0bec5;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#78909c;stop-opacity:1" />
</radialGradient>

<!-- Colored Components (Fan Blades, Flow, etc.) -->
<linearGradient id="blueComponentGradient" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#64b5f6;stop-opacity:1" />
  <stop offset="50%" style="stop-color:#2196f3;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#1976d2;stop-opacity:1" />
</linearGradient>
```

## Filter Template

```xml
<!-- Light Theme Drop Shadow (Subtler) -->
<filter id="dropShadow" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="2"/>
  <feOffset dx="0" dy="2" result="offsetblur"/>
  <feComponentTransfer>
    <feFuncA type="linear" slope="0.12"/>  <!-- Lighter shadows -->
  </feComponentTransfer>
  <feMerge>
    <feMergeNode/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

## Accessibility Considerations

The light theme provides:
- ✅ Higher contrast for ambient lighting environments
- ✅ Reduced eye strain in well-lit control rooms
- ✅ Better readability for printed documentation
- ✅ WCAG AA compliant text contrast (4.5:1 minimum)
- ✅ Maintains color-blind friendly status indicators

## Testing Checklist

For each converted widget, verify:
- [ ] Background is light (`#f5f7fa` or `#ffffff`)
- [ ] All text is dark and readable
- [ ] Gradients use light → medium grays
- [ ] Shadows are subtle (opacity < 0.15)
- [ ] Status colors (green/orange/red) unchanged
- [ ] Borders/strokes are visible but not harsh
- [ ] Animations work correctly
- [ ] All FUXA variables intact
- [ ] CSV catalog datapoints match

---

**Created**: 2025-10-17
**Purpose**: Complete guide for converting all 51 widgets to light theme
**Status**: Ready for implementation
