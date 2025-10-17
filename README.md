# WBG Widgets - BMS Device SVG Widget Library

A comprehensive collection of **44 professional SVG widgets** for Building Management Systems (BMS), HVAC control, and SCADA applications. All widgets feature a **modern light theme** and are **100% mapped to the BMS Device Datapoint Catalog** for complete integration with real-world BMS systems.

## ✨ **NEW: All 44 widgets converted to professional light theme!**

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Widget Categories](#widget-categories)
- [CSV Catalog Integration](#csv-catalog-integration)
- [Installation](#installation)
- [Usage with FUXA](#usage-with-fuxa)
- [Enhanced Design System](#enhanced-design-system)
- [License](#license)

## 🎯 Overview

This library provides ready-to-use SVG widgets for building automation systems, with **all datapoints mapped directly to BMS_Device_Datapoint_Catalog.csv**. Each widget includes:

- **CSV-Aligned Datapoints** - Every variable matches the catalog exactly
- **Enhanced Visual Design** - Professional QA Graphics-inspired styling
- **Embedded JavaScript** for dynamic updates and interactivity
- **FUXA-compatible variable binding** for seamless integration
- **Real-time animations** for status indicators, fans, pumps, and flow visualization
- **Responsive design** that scales perfectly at any resolution

## ✨ Features

- **CSV Catalog-Driven** - All widgets match BMS_Device_Datapoint_Catalog.csv
- **Zero Dependencies** - Pure SVG + JavaScript
- **Self-Contained** - All logic embedded in SVG files
- **FUXA Standard Format** - All widgets use proper export/putValue/update pattern
- **Dark Theme** optimized for control room displays
- **Professional Graphics** - Gradients, shadows, and depth for realistic rendering
- **Color-Coded Status** - Green (normal), Yellow (warning), Red (alarm), Blue (cooling)
- **Interactive Controls** - Buttons, sliders, toggles with visual feedback
- **Animated Elements** - Rotating fans/pumps, flowing air/water, blinking alarms

## 📁 Widget Categories

### 1. Primitives (20 widgets)
Basic building blocks for HVAC and BMS systems:

**Enhanced Samples:**
- ✅ **fan-enhanced.svg** - 3D fan with rotation animation, status ring, smart speed detection

**Standard Widgets:**
- **Fans**: `fan.svg`, `fan-3speed.svg`
- **Valves**: `valve-2pos.svg`, `valve-analog.svg`, `valve-3way.svg`
- **Dampers**: `damper.svg`, `damper-2pos.svg`
- **Pumps**: `pump.svg`, `pump-vfd.svg`
- **Sensors**: `sensor-chip-temp.svg`, `sensor-chip-humidity.svg`, `sensor-chip-pressure.svg`, `sensor-chip-co2.svg`
- **Components**: `alarm-chip.svg`, `filter.svg`, `heater.svg`, `coil-heating.svg`, `coil-cooling.svg`, `compressor.svg`, `motor.svg`

### 2. HVAC (12 widgets)
Complete HVAC equipment matching CSV catalog:

**Enhanced Samples:**
- ✅ **vav-enhanced.svg** - Full VAV Box with 11 CSV-aligned datapoints, rotating damper, airflow animation

**Standard Widgets:**
- `ahu-compact.svg` - Air Handling Unit (compact view)
- `ahu-detailed.svg` - Air Handling Unit (detailed view)
- `fcu.svg` - Fan Coil Unit
- `rtu.svg` - Rooftop Unit
- `vav.svg` - Variable Air Volume box
- `vav-reheat.svg` - VAV with reheat coil
- `exhaust-fan.svg` - Exhaust fan system
- `heat-exchanger.svg` - Heat recovery unit
- `humidifier.svg` - Humidification system
- `dehumidifier.svg` - Dehumidification system
- `economizer.svg` - Economizer damper assembly

### 3. Utilities (8+ widgets)
Utility metering and backup power systems:

**Enhanced Samples:**
- ✅ **power-meter-enhanced.svg** - Professional power meter with circular gauge, LED displays, 9 CSV datapoints
- ✅ **bess.svg** - NEW: Battery Energy Storage System with SOC animation, flow diagram, 6 CSV datapoints

**Standard Widgets:**
- `electrical-meter.svg` - Power meter
- `water-meter.svg` - Water meter
- `gas-meter.svg` - Gas meter
- `btu-meter.svg` - Thermal/Energy meter
- `switch-breaker.svg` - Circuit breaker
- `transformer.svg` - Transformer
- `generator.svg` - Emergency generator
- `ups.svg` - UPS system

## 🗂️ CSV Catalog Integration

All widgets are **100% aligned** with **BMS_Device_Datapoint_Catalog.csv**. The catalog contains **40 device types** with complete datapoint specifications:

### Device Coverage

**✅ Currently Implemented:**
- AHU, VAV Box, FCU, RTU, DOAS (HVAC air systems)
- CRAC/CRAH (Data center cooling)
- Chiller, Boiler, Cooling Tower, Pumps (Central plant)
- VFD, Valves, Dampers, Fans (Primitives)
- Sensors (Temp, Humidity, Pressure, CO2, PM2.5, VOC, Occupancy, Smoke, Leak)
- Power Meter, Water Meter, Gas Meter, Thermal Meter (Utilities)
- Thermostat/Zone Control
- UPS, Generator
- **BESS** (Battery Energy Storage) - NEW!

**⏳ Planned (Missing from Current Library):**
- ATS (Automatic Transfer Switch)
- Access Control (Door status, events)
- CDU (Coolant Distribution Unit - data center)
- DHW Heater (Domestic Hot Water)
- EVSE (Electric Vehicle Charger)
- Elevator (Status monitoring)
- Fire Alarm Panel
- PV Inverter (Solar)
- Plate Heat Exchanger
- Shade Controller
- Light Signal (Binary & Dimmer)

### Variable Naming Convention

All widgets follow FUXA standard prefixes:

- `_pn_` = **Numeric** (temperature, speed, position, flow, etc.)
- `_pb_` = **Boolean** (alarm, enabled, occupied, etc.)
- `_ps_` = **String** (text codes, labels, modes)

### Example: VAV Box Datapoints (from CSV)

```javascript
//!export-start
let _pn_airflow = 450;              // Airflow (CFM/L/s) - From flow sensor
let _pn_airflowSP = 500;            // Airflow SP (CFM/L/s)
let _pn_damperCommand = 65;         // Damper Command (0-100%)
let _pn_damperPosition = 65;        // Damper Position (0-100%) - Feedback
let _pn_zoneTemp = 72.5;            // Zone Temp (°F/°C)
let _pn_zoneTempSPOcc = 72.0;       // Zone Temp SP Occ (°F/°C)
let _pn_zoneTempSPUnocc = 76.0;     // Zone Temp SP Unocc (°F/°C)
let _pn_reheatStatus = 0;           // Reheat Status (On/Off/%)
let _pn_reheatValveCmd = 0;         // Reheat Valve Cmd (0-100%)
let _pb_occupancy = true;           // Occupancy (Occ/Unocc)
let _pb_alarmActive = false;        // Alarms (Text/Code)
//!export-end
```

## 🚀 Installation

### Option 1: Direct Download
1. Clone or download this repository
2. Copy the widget folders to your FUXA project directory

### Option 2: Git Submodule
```bash
cd your-fuxa-project
git submodule add https://github.com/yourusername/wbg_widgets.git widgets
```

### Option 3: Individual Widgets
Copy only the widgets you need from the category folders.

## 📖 Usage with FUXA

### Basic Integration

1. **Import Widget into FUXA**:
   - Open FUXA editor
   - Navigate to Graphics → SVG Library
   - Click "Import SVG"
   - Select the desired widget file

2. **Add to View**:
   - Drag the imported widget onto your view
   - Resize and position as needed

3. **Bind Variables**:
   - Select the widget
   - Open Properties panel
   - Map FUXA tags/devices to widget variables

### Example: Binding Enhanced VAV Box

```javascript
// In FUXA, bind these variables to your device tags:
_pn_airflow → "PLC.AHU1_VAV_101.Airflow"
_pn_damperPosition → "PLC.AHU1_VAV_101.DamperPos"
_pn_zoneTemp → "PLC.AHU1_VAV_101.ZoneTemp"
_pn_zoneTempSPOcc → "PLC.AHU1_VAV_101.SetpointOcc"
_pb_occupancy → "PLC.AHU1_VAV_101.Occupied"
_pb_alarmActive → "PLC.AHU1_VAV_101.Alarm"
```

The widget will automatically:
- Rotate damper blade based on position (0-90°)
- Display airflow with animated particles
- Show occupancy-based setpoint
- Detect flow errors (±15% tolerance)
- Pulse alarm indicator if active

## 🎨 Enhanced Design System

Four sample **enhanced widgets** demonstrate the new professional visual design:

### Visual Features

✅ **Depth & Dimensionality**
- Linear/radial gradients for realistic depth
- Drop shadows and glow effects
- Multi-layer component rendering
- Highlight overlays for reflective surfaces

✅ **Professional Typography**
- Headers: 'Segoe UI' / Arial
- Values: 'Orbitron' / 'Consolas' (digital display aesthetic)
- Consistent sizing hierarchy

✅ **Enhanced Color Palette**
```css
/* Status */
Normal/On:     #27ae60 (Green)
Warning:       #f39c12 (Orange)
Alarm:         #e74c3c (Red)
Inactive:      #7f8c8d (Gray)
Info/Cooling:  #3498db (Blue)
LED Display:   #00ff88 (Bright Green)
Accent:        #00d4ff (Cyan)

/* Components */
Enclosures:    #455a64 → #263238 (Gradient)
Ductwork:      #90a4ae → #607d8b (Gradient)
Background:    #1a1a2e (Dark)
Panels:        #2c3e50 / #34495e (Charcoal)
```

✅ **Smooth Animations**
- Rotation animations (fans, pumps)
- Pulsing effects (charging, alarms)
- Flow animations (air, water, energy)
- All CSS-based for performance

### Enhanced Widgets

1. **[fan-enhanced.svg](primitives/fan-enhanced.svg)** - Primitive
   - 3D housing with dual-ring detail
   - Four-blade design with shadows
   - Status ring with circular progress
   - Speed-based rotation

2. **[vav-enhanced.svg](hvac/vav-enhanced.svg)** - HVAC Device
   - Metallic gradient ductwork
   - Rotating damper (0-90°)
   - Animated airflow particles
   - 11 CSV-aligned datapoints

3. **[power-meter-enhanced.svg](utilities/power-meter-enhanced.svg)** - Meter
   - Professional bezel frame
   - LED-style displays with glow
   - Circular gauge (color-coded)
   - 9 CSV-aligned datapoints

4. **[bess.svg](utilities/bess.svg)** - NEW Device Type
   - Battery cells with SOC fill animation
   - Directional power flow diagram
   - Charging/discharging detection
   - 6 CSV-aligned datapoints

See **[ENHANCED_WIDGETS_GUIDE.md](ENHANCED_WIDGETS_GUIDE.md)** for complete design system documentation.

## 🛠️ Development

### Widget Structure

Each widget follows this structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 width height">
  <defs>
    <style>
      /* CSS styles, gradients, animations */
    </style>
    <!-- Gradients and filters -->
  </defs>

  <!-- SVG graphics elements -->

  <script type="text/javascript">
    <![CDATA[
    //!export-start
    let _pn_variable = 0;  // Exported variables
    //!export-end

    function update() {
      // Update graphics based on variables
    }

    function putValue(id, value) {
      // FUXA calls this to update values
      update();
    }

    init();
    ]]>
  </script>
</svg>
```

### Design Standards

- **File Naming**: Lowercase with hyphens (e.g., `vav-enhanced.svg`)
- **Primitives viewBox**: `0 0 100-120 100-120`
- **Cards viewBox**: `0 0 400-450 300-400`
- **No titles in widgets** - Titles added by user in FUXA
- **All datapoints from CSV** - No custom/non-standard variables

## 📚 Documentation

- **[BMS_Device_Datapoint_Catalog.csv](BMS_Device_Datapoint_Catalog.csv)** - Complete device/datapoint catalog
- **[ENHANCED_WIDGETS_GUIDE.md](ENHANCED_WIDGETS_GUIDE.md)** - Design system guide and enhanced widget details
- **[README.md](README.md)** - This file

## 🤝 Contributing

Contributions are welcome! To add new widgets or improve existing ones:

1. Fork the repository
2. Ensure widget matches CSV catalog datapoints exactly
3. Follow the enhanced design system standards
4. Test your widget in FUXA
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Inspired by [QA Graphics Vector Symbol Library](https://www.qagraphics.com/vector-symbol-lib/)
- Built for the [FUXA SCADA platform](https://github.com/frangoteam/FUXA)
- Designed for building automation and BMS applications

## 🗺️ Roadmap

### Phase 1: Complete CSV Catalog Coverage
- [ ] Rebuild all primitives with enhanced design
- [ ] Rebuild all HVAC devices
- [ ] Add missing devices (ATS, CDU, EVSE, etc.)

### Phase 2: Advanced Features
- [ ] Multi-language label support
- [ ] Unit conversion (°F/°C, CFM/L/s, etc.)
- [ ] Touch-optimized controls
- [ ] Accessibility improvements

### Phase 3: Documentation
- [ ] Widget preview gallery
- [ ] Interactive configuration wizard
- [ ] Video tutorials

---

**Version**: 2.0.0
**Last Updated**: 2025-10-17
**CSV Catalog**: BMS_Device_Datapoint_Catalog.csv
**Enhanced Widgets**: 4 samples available

Made for the Building Automation community
