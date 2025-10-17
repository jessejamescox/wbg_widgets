# Enhanced Widget Library - Design System Guide

## Overview

This guide documents the enhanced widget design system that aligns with professional BMS/SCADA visualization standards inspired by QA Graphics vector symbol libraries.

## Sample Enhanced Widgets

Four sample enhanced widgets have been created to demonstrate the new visual design system:

1. **[fan-enhanced.svg](primitives/fan-enhanced.svg)** - Enhanced Primitive Component
2. **[vav-enhanced.svg](hvac/vav-enhanced.svg)** - Enhanced HVAC Device
3. **[power-meter-enhanced.svg](utilities/power-meter-enhanced.svg)** - Enhanced Utility Meter
4. **[bess.svg](utilities/bess.svg)** - New Missing Device Type

---

## Design Principles

### Visual Enhancement Features

#### 1. **Depth & Dimensionality**
- Linear and radial gradients for realistic depth
- Drop shadows with configurable blur and opacity
- Multi-layer component rendering
- Highlight overlays for reflective surfaces

#### 2. **Professional Typography**
- **Headers**: 'Segoe UI' / Arial - Clean, modern sans-serif
- **Values**: 'Orbitron' / 'Consolas' / Monospace - Digital display aesthetic
- **Labels**: Consistent sizing hierarchy (18px titles, 11px labels, 13-22px values)
- Letter-spacing for technical readability

#### 3. **Color System Enhancements**

##### Status Colors
```css
Normal/On:     #27ae60 (Green)
Warning:       #f39c12 (Orange/Yellow)
Alarm/Stop:    #e74c3c (Red)
Inactive/Off:  #7f8c8d (Gray)
Info/Cooling:  #3498db (Blue)
Data Display:  #00ff88 (Bright Green - LED style)
Accent:        #00d4ff (Cyan)
```

##### Component Colors
```css
Enclosures:    #455a64 → #263238 (Gray-blue gradient)
Ductwork:      #90a4ae → #607d8b (Silver-gray gradient)
Background:    #1a1a2e (Dark blue-black)
Panels:        #2c3e50 → #34495e (Charcoal)
```

#### 4. **Animation & Interactivity**

##### Rotation Animations
- Fan blades rotate based on speed percentage
- Smooth frame-rate (50ms intervals)
- Speed-proportional rotation rates

##### Pulsing Effects
```css
@keyframes powerPulse {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 1; }
}

@keyframes alarmFlash {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}
```

##### Flow Animations
- Airflow particles with staggered delays
- CSS-based flow pulse for performance
- Conditional display based on equipment status

#### 5. **Modular Component Design**

##### Reusable SVG Elements
- Defined gradients in `<defs>` section
- Shared filters (dropShadow, glow, blur)
- Component-based structure for easy modification

##### Standardized Dimensions
- Primitives: 100-120px square
- Cards/Panels: 400-450px width
- Consistent padding: 10-20px
- Border radius: 4-10px for modern aesthetic

---

## Widget-Specific Implementation

### 1. Enhanced Fan Primitive ([fan-enhanced.svg](primitives/fan-enhanced.svg))

#### Visual Features
- **3D housing** with gradient fill and dual-ring detail
- **Four-blade design** with individual shadows
- **Center hub** with multi-layer depth (11px → 8px → 4px radii)
- **Status ring** (top-right) with stroke-dasharray progress indicator
- **Info panel** with speed percentage and status text

#### Datapoints (CSV Aligned)
```javascript
_pn_status      // Fan status: 0=off, 1=on
_pn_speed       // Fan speed percentage (0-100%)
_pn_alarm       // Alarm state: 0=normal, 1=alarm
```

#### Animation Details
- Rotation speed: `_pn_speed / 8` degrees per frame
- Status ring fill: Circular progress from 0-100%
- Speed categories: LOW (<30%), MEDIUM (30-70%), HIGH (>70%)

---

### 2. Enhanced VAV Box ([vav-enhanced.svg](hvac/vav-enhanced.svg))

#### Visual Features
- **Supply and zone ductwork** with gradient metallic finish
- **VAV enclosure** with top highlight for reflectivity
- **Rotating damper blade** with shaft and actuator indicator
- **Airflow particles** with staggered CSS animations
- **Six-value data panel** with grouped sections

#### Datapoints (CSV Aligned)
All datapoints match **BMS_Device_Datapoint_Catalog.csv - VAV Box**:
```javascript
_pn_airflow              // Airflow (CFM/L/s) - From flow sensor
_pn_airflowSP            // Airflow SP (CFM/L/s)
_pn_damperCommand        // Damper Command (0-100%)
_pn_damperPosition       // Damper Position (0-100%) - Feedback
_pn_zoneTemp             // Zone Temp (°F/°C)
_pn_zoneTempSPOcc        // Zone Temp SP Occ (°F/°C)
_pn_zoneTempSPUnocc      // Zone Temp SP Unocc (°F/°C)
_pn_reheatStatus         // Reheat Status (On/Off/%)
_pn_reheatValveCmd       // Reheat Valve Cmd (0-100%)
_pb_occupancy            // Occupancy (Occ/Unocc)
_pb_alarmActive          // Alarms (Text/Code)
```

#### Smart Logic
- Damper rotates 0-90° based on position feedback
- Flow error detection (±15% tolerance)
- Occupancy-based setpoint display
- Automatic flow animation cutoff when damper <5% or airflow <50 CFM

---

### 3. Enhanced Power Meter ([power-meter-enhanced.svg](utilities/power-meter-enhanced.svg))

#### Visual Features
- **Bezel frame** with metallic gradient
- **LED-style displays** with "Orbitron" font and glow filter
- **Circular power gauge** with color-coded segments
- **Power bar indicator** with gradient (green → orange → red)
- **Six-parameter grid** layout

#### Datapoints (CSV Aligned)
All datapoints match **BMS_Device_Datapoint_Catalog.csv - Power Meter**:
```javascript
_pn_realPower       // Real Power (kW)
_pn_voltage         // Voltage Ph-Ph (V)
_pn_current         // Current per phase (A)
_pn_powerFactor     // Power Factor (PF)
_pn_frequency       // Frequency (Hz)
_pn_energy          // Energy (kWh)
_pn_demand          // Demand (kW)
_pn_alarm           // Alarm status (0=normal, 1=alarm)
_pn_maxPower        // Maximum power rating (kW)
```

#### Dynamic Behaviors
- **Power gauge** changes color based on % load:
  - 0-60%: Green with pulse animation
  - 60-85%: Orange
  - 85-100%: Red
- **Power factor indicator**:
  - ≥0.95: Green (good)
  - 0.85-0.95: Yellow (warning)
  - <0.85: Red (poor)
- **Status light**: Considers load % and PF for overall health

---

### 4. BESS - Battery Energy Storage System ([bess.svg](utilities/bess.svg))

#### Visual Features (New Device Type)
- **Battery container** with four visible cells and terminals
- **SOC fill animation** (bottom-up liquid fill effect)
- **Power flow diagram** with directional arrows
- **Mode indicator** with pulsing effects
- **Five-value data panel** (Power, Mode, SOC, SOH, Alarms)

#### Datapoints (CSV Aligned)
All datapoints match **BMS_Device_Datapoint_Catalog.csv - BESS**:
```javascript
_pn_chargeDischargePower  // Charge/Discharge Power (kW)
_pn_soc                   // SOC (%) - State of Charge
_pn_soh                   // SOH (%) - State of Health
_pn_modeCmd               // Mode Cmd (0=Idle, 1=Charge, 2=Discharge)
_ps_alarms                // Alarms (Text/Code)
_pb_alarmActive           // Alarm active boolean
```

#### Smart Logic
- **SOC fill color**:
  - <20%: Red gradient
  - 20-50%: Orange gradient
  - >50%: Green gradient
- **Flow direction**:
  - Charging: Arrow down (grid → battery), green
  - Discharging: Arrow up (battery → grid), blue
  - Idle: No animation, gray
- **Power sign convention**: Positive = discharge, Negative = charge
- **Mode auto-detection**: Can work from `_pn_modeCmd` OR `_pn_chargeDischargePower` sign

---

## CSS/SVG Techniques Used

### 1. Gradients
```xml
<linearGradient id="enclosureGradient" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#546e7a;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#37474f;stop-opacity:1" />
</linearGradient>
```

### 2. Filters
```xml
<filter id="dropShadow">
  <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
  <feOffset dx="0" dy="3"/>
  <feComponentTransfer>
    <feFuncA type="linear" slope="0.3"/>
  </feComponentTransfer>
  <feMerge>
    <feMergeNode/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

### 3. Stroke Dasharray for Progress
```javascript
const circumference = 2 * Math.PI * radius;
const offset = circumference - (percentage / 100) * circumference;
element.setAttribute('stroke-dashoffset', offset);
```

---

## CSV Catalog Integration

All enhanced widgets map directly to **BMS_Device_Datapoint_Catalog.csv**:

| Widget | Device Type | Datapoints | Status |
|--------|-------------|------------|--------|
| fan-enhanced.svg | Fan/Pump (Generic) | 3 | ✅ Complete |
| vav-enhanced.svg | VAV Box | 11 | ✅ Complete |
| power-meter-enhanced.svg | Power Meter | 9 | ✅ Complete |
| bess.svg | BESS | 6 | ✅ New Device |

### Variable Naming Convention
- `_pn_` = Numeric (position, speed, temperature, etc.)
- `_pb_` = Boolean (alarm, status, occupancy)
- `_ps_` = String (text codes, labels)

---

## Next Steps for Full Rebuild

### Phase 1: Primitives (20 widgets)
- [ ] Enhanced valves (2-pos, analog, 3-way)
- [ ] Enhanced dampers (2-pos, analog)
- [ ] Enhanced pumps (VFD)
- [ ] Enhanced sensors (temp, humidity, pressure, CO2, PM2.5, VOC)
- [ ] Enhanced coils (heating, cooling)
- [ ] Enhanced compressor, motor, filter, heater

### Phase 2: HVAC Systems (12 widgets)
- [ ] AHU (compact & detailed)
- [ ] FCU, RTU, DOAS
- [ ] Heat exchanger, economizer
- [ ] Humidifier, dehumidifier
- [ ] CRAC/CRAH

### Phase 3: Utilities (8 widgets)
- [ ] Water, Gas, BTU meters
- [ ] Switch/breaker, transformer
- [ ] Generator, UPS

### Phase 4: Missing Devices (11 new widgets)
- [ ] ATS (Automatic Transfer Switch)
- [ ] Access Control
- [ ] CDU (Coolant Distribution Unit)
- [ ] DHW Heater
- [ ] EVSE (EV Charger)
- [ ] Elevator
- [ ] Fire Alarm Panel
- [ ] Plate Heat Exchanger
- [ ] Shade Controller
- [ ] Light Signal (Binary & Dimmer)

### Phase 5: Central Plant
- [ ] Chiller
- [ ] Boiler
- [ ] Cooling Tower

---

## Design System Standards

### File Naming
- Lowercase with hyphens: `vav-enhanced.svg`
- Descriptive device type names
- Use `-enhanced` suffix during transition period

### viewBox Standards
- Primitives: `0 0 100-120 100-120`
- Cards: `0 0 400-450 300-400`
- Meters: `0 0 400-450 500-600`

### Color Palette Reference
```css
/* Backgrounds */
--bg-primary: #1a1a2e;
--bg-secondary: #2c3e50;
--bg-tertiary: #34495e;

/* Text */
--text-primary: #ecf0f1;
--text-secondary: #bdc3c7;
--text-tertiary: #95a5a6;

/* Accent */
--accent-cyan: #00d4ff;
--accent-blue: #3498db;
--accent-green: #00ff88;

/* Status */
--status-ok: #27ae60;
--status-warning: #f39c12;
--status-alarm: #e74c3c;
--status-inactive: #7f8c8d;

/* Components */
--component-metal: #546e7a → #37474f;
--component-duct: #90a4ae → #607d8b;
```

---

## Performance Considerations

### Animation Best Practices
- Use CSS animations over JavaScript where possible
- Limit active setInterval() calls (clear when not needed)
- Use `requestAnimationFrame` for smooth 60fps (future enhancement)
- Stagger animation delays for visual interest

### SVG Optimization
- Minimize filter usage (2-3 max per widget)
- Reuse gradients and filters via `<defs>`
- Use transform-origin for rotation instead of recalculating coordinates
- Keep path data concise

---

## FUXA Integration

All enhanced widgets maintain full FUXA compatibility:

1. **Export variables** between `//!export-start` and `//!export-end`
2. **putValue() function** for FUXA to update values
3. **init() function** called on load
4. **update() function** for internal state refresh

### Example Binding
```javascript
// In FUXA, bind these variables:
_pn_airflow → Tag: "AHU1.VAV_101.Airflow"
_pn_zoneTemp → Tag: "AHU1.VAV_101.ZoneTemp"
```

---

**Created**: 2025-10-17
**Design Standard**: QA Graphics Vector Symbol Library
**CSV Catalog Version**: BMS_Device_Datapoint_Catalog.csv
**Status**: Sample Widgets Complete - Ready for Full Rebuild
