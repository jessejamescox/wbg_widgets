# WBG Widgets - Building Automation SVG Widget Library

A comprehensive collection of **82 professional SVG widgets** for Building Management Systems (BMS), HVAC control, and SCADA applications. All widgets are designed for [FUXA](https://github.com/frangoteam/FUXA) integration with embedded JavaScript for real-time data binding and control.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Widget Categories](#widget-categories)
- [Installation](#installation)
- [Usage with FUXA](#usage-with-fuxa)
- [Widget Documentation](#widget-documentation)
- [Customization](#customization)
- [License](#license)

## 🎯 Overview

This library provides ready-to-use SVG widgets for building automation and industrial SCADA systems. Each widget includes:

- **Embedded JavaScript** for dynamic updates and interactivity
- **FUXA-compatible variable binding** for seamless integration
- **Professional BMS styling** with industry-standard color coding
- **Real-time animations** for status indicators, fans, pumps, and flow visualization
- **Responsive design** that scales perfectly at any resolution

## ✨ Features

- **82 Total Widgets** across 10 categories
- **Zero Dependencies** - Pure SVG + JavaScript
- **Self-Contained** - All logic embedded in SVG files
- **Dark Theme** optimized for control room displays
- **Color-Coded Status** - Green (normal), Yellow (warning), Red (alarm), Blue (cooling), Orange (heating)
- **Interactive Controls** - Buttons, sliders, toggles with visual feedback
- **Animated Elements** - Rotating fans/pumps, flowing liquids, blinking alarms
- **Alarm Handling** - Built-in alarm states and visual indicators
- **Real-Time Updates** - 50-100ms refresh rates for smooth visualization

## 📁 Widget Categories

### 1. Primitives (20 widgets)
Basic building blocks for HVAC and BMS systems:

- **Fans**: `fan.svg`, `fan-3speed.svg`
- **Valves**: `valve-2pos.svg`, `valve-analog.svg`, `valve-3way.svg`
- **Dampers**: `damper.svg`, `damper-2pos.svg`
- **Pumps**: `pump.svg`, `pump-vfd.svg`
- **Sensors**: `sensor-chip-temp.svg`, `sensor-chip-humidity.svg`, `sensor-chip-pressure.svg`, `sensor-chip-co2.svg`
- **Components**: `alarm-chip.svg`, `filter.svg`, `heater.svg`, `coil-heating.svg`, `coil-cooling.svg`, `compressor.svg`, `motor.svg`

### 2. HVAC (12 widgets)
Complete HVAC equipment and air handling:

- `thermostat-card.svg` - Interactive thermostat control
- `vav.svg` - Variable Air Volume box
- `vav-reheat.svg` - VAV with reheat coil
- `ahu-compact.svg` - Compact Air Handling Unit
- `ahu-detailed.svg` - Detailed AHU with all components
- `fcu.svg` - Fan Coil Unit
- `rtu.svg` - Rooftop Unit
- `exhaust-fan.svg` - Exhaust fan system
- `heat-exchanger.svg` - Heat recovery unit
- `humidifier.svg` - Humidification system
- `dehumidifier.svg` - Dehumidification system
- `economizer.svg` - Economizer damper assembly

### 3. Systems (10 widgets)
Large-scale building systems and plants:

- `chiller-plant.svg` - Multi-chiller plant with cooling towers
- `chiller-air-cooled.svg` - Air-cooled chiller
- `chiller-water-cooled.svg` - Water-cooled chiller
- `cooling-tower.svg` - Cooling tower
- `boiler.svg` - Boiler system
- `boiler-plant.svg` - Multi-boiler plant
- `heat-pump.svg` - Heat pump system
- `vrf-system.svg` - VRF/VRV system
- `primary-secondary.svg` - Primary-secondary pumping
- `waterside-economizer.svg` - Waterside economizer

### 4. Zones (5 widgets)
Space and zone-level controls:

- `zone-temp-card.svg` - Zone temperature display
- `room-comfort.svg` - Multi-parameter room comfort
- `occupancy-card.svg` - Occupancy monitoring
- `conference-room.svg` - Conference room control
- `office-zone.svg` - Multi-space office zone

### 5. Utilities (8 widgets)
Utility metering and monitoring:

- `electrical-meter.svg` - Power meter
- `water-meter.svg` - Water meter
- `gas-meter.svg` - Gas meter
- `btu-meter.svg` - Energy meter
- `switch-breaker.svg` - Circuit breaker
- `transformer.svg` - Transformer
- `generator.svg` - Emergency generator
- `ups.svg` - UPS system

### 6. Controls (6 widgets)
Interactive control interfaces:

- `button-on-off.svg` - Toggle button
- `button-start-stop.svg` - Start/Stop button
- `slider-setpoint.svg` - Setpoint slider
- `pid-controller.svg` - PID controller card
- `schedule-card.svg` - Schedule display
- `override-card.svg` - Override control

### 7. Indicators (7 widgets)
Display and visualization elements:

- `gauge-semicircle.svg` - 180° gauge
- `gauge-radial.svg` - Full circular gauge
- `gauge-horizontal.svg` - Bar gauge
- `trend-mini.svg` - Mini trend chart
- `status-led.svg` - LED indicator
- `alarm-banner.svg` - Alarm banner
- `mode-indicator.svg` - Mode display

### 8. Tanks (4 widgets)
Liquid storage and containment:

- `water-tank.svg` - Water storage tank
- `fuel-tank.svg` - Fuel tank
- `buffer-tank.svg` - Thermal storage tank
- `expansion-tank.svg` - Expansion tank

### 9. Safety (4 widgets)
Life safety systems:

- `smoke-detector.svg` - Smoke detector
- `fire-damper.svg` - Fire damper
- `fire-alarm.svg` - Fire alarm panel
- `emergency-light.svg` - Emergency lighting

### 10. Specialty (5 widgets)
Specialized equipment:

- `elevator-status.svg` - Elevator status
- `door-contact.svg` - Door sensor
- `weather-station.svg` - Weather data
- `solar-panel.svg` - Solar monitoring
- `battery-storage.svg` - Battery storage

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
   - Map FUXA tags to widget variables

### Example: Binding a Fan Widget

```javascript
// Widget exposes these variables:
// - status: 0=off, 1=on
// - speed: 0-100 (%)
// - alarmState: 0=normal, 1=alarm

// In FUXA, bind:
status → PLC.AHU1_SF_Status
speed → PLC.AHU1_SF_Speed
alarmState → PLC.AHU1_SF_Alarm
```

### Example: Thermostat Control

```javascript
// Widget variables:
// - currentTemp: Current temperature
// - setpoint: Temperature setpoint
// - mode: 0=Off, 1=Heat, 2=Cool, 3=Auto
// - fanMode: 0=Auto, 1=On

// Bidirectional binding:
currentTemp → PLC.Zone1_Temp (read)
setpoint ⟷ PLC.Zone1_Setpoint (read/write)
mode ⟷ PLC.Zone1_Mode (read/write)
fanMode ⟷ PLC.Zone1_Fan (read/write)
```

## 📚 Widget Documentation

### Common Variables

Most widgets share these common variable patterns:

#### Status Variables
- `status` - Equipment status (0=off, 1=on)
- `alarmState` - Alarm condition (0=normal, 1=alarm)
- `enabled` - Enable/disable (0=disabled, 1=enabled)

#### Analog Variables
- `position` - Position 0-100%
- `speed` - Speed 0-100%
- `capacity` - Capacity/load 0-100%
- `temperature` - Temperature value
- `pressure` - Pressure value
- `flow` - Flow rate

#### Control Variables
- `command` - Commanded value
- `feedback` - Feedback/actual value
- `setpoint` - Setpoint value
- `mode` - Operating mode

### Color Coding Standards

| Color | Hex | Usage |
|-------|-----|-------|
| Green | #27ae60 | Normal status, Go, On |
| Red | #e74c3c | Alarm, Stop, Emergency |
| Yellow/Orange | #f39c12 | Warning, Caution |
| Blue | #3498db | Cooling, Water, Info |
| Gray | #95a5a6 | Off, Disabled, Inactive |
| Dark Blue | #34495e | Heating (darker) |

### Temperature Color Ranges

- **Cold** (< 50°F / 10°C): Light Blue #5dade2
- **Cool** (50-65°F / 10-18°C): Blue #3498db
- **Neutral** (65-75°F / 18-24°C): Green #27ae60
- **Warm** (75-85°F / 24-29°C): Orange #f39c12
- **Hot** (> 85°F / 29°C): Red #e74c3c

## 🎨 Customization

### Modifying Widget Colors

Open any SVG file and edit the `<style>` section:

```svg
<defs>
  <style>
    .fan-status-on { fill: #27ae60; }  /* Change green color */
    .fan-status-off { fill: #95a5a6; } /* Change gray color */
  </style>
</defs>
```

### Adjusting Variable Names

Edit the JavaScript section in the SVG:

```javascript
// Original:
var status = 0;
var speed = 0;

// Rename to match your naming convention:
var fanStatus = 0;
var fanSpeed = 0;
```

### Changing Animation Speed

Modify the interval timing:

```javascript
// Original (fast):
setInterval(function() {
  rotation += 10;
  // ...
}, 50);

// Slower:
setInterval(function() {
  rotation += 5;
  // ...
}, 100);
```

### Adding Custom Logic

Extend the `updateWidget()` function:

```javascript
function updateWidget() {
  // Existing code...

  // Add custom logic:
  if (speed > 80) {
    console.log('High speed warning');
    // Trigger custom animation
  }
}
```

## 🔧 Advanced Features

### Multi-Language Support

Add language variables to widgets:

```javascript
var lang = 'en'; // 'en', 'es', 'fr', etc.
var labels = {
  en: { on: 'ON', off: 'OFF' },
  es: { on: 'ENCENDIDO', off: 'APAGADO' }
};
statusText.textContent = labels[lang][status ? 'on' : 'off'];
```

### Unit Conversion

Add unit conversion functions:

```javascript
var units = 'F'; // 'F' or 'C'
function displayTemp(tempF) {
  if (units === 'C') {
    return ((tempF - 32) * 5/9).toFixed(1) + '°C';
  }
  return tempF.toFixed(1) + '°F';
}
```

### Historical Trending

Some widgets (like `trend-mini.svg`) support historical data:

```javascript
var historyData = []; // Array of up to 24 values
var historyMax = 24;

function addDataPoint(value) {
  historyData.push(value);
  if (historyData.length > historyMax) {
    historyData.shift();
  }
  updateTrendChart();
}
```

## 🛠️ Development

### Widget Structure

Each widget follows this structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <defs>
    <style>
      /* CSS styles */
    </style>
  </defs>

  <!-- SVG graphics elements -->

  <script type="text/javascript">
    <![CDATA[
    // Exported variables
    var status = 0;

    // Update function
    function updateWidget() {
      // Update graphics based on variables
    }

    // Initialize
    updateWidget();
    ]]>
  </script>
</svg>
```

### Creating Custom Widgets

1. **Start with a template** from the primitives folder
2. **Design the graphics** using SVG elements
3. **Add CSS styles** in the `<defs>` section
4. **Define variables** in the `<script>` section
5. **Implement updateWidget()** to refresh the display
6. **Test** with different values

### Best Practices

- Use semantic variable names (e.g., `supplyTemp` not `temp1`)
- Include units in labels (°F, PSI, GPM, etc.)
- Add comments explaining complex logic
- Test with extreme values (0, 100, negative)
- Ensure animations don't impact performance
- Use `requestAnimationFrame` for smooth animations
- Implement bounds checking (min/max values)

## 📝 Variable Reference

### Complete Variable List by Category

#### Primitives
- **Fan**: status, speed, alarmState
- **Valve (2-pos)**: position, feedback
- **Valve (Analog)**: position, command, feedback
- **Valve (3-way)**: position
- **Damper**: position, command, feedback
- **Pump**: status, alarmState, runCommand, runFeedback
- **Pump (VFD)**: speed, status, frequency
- **Sensors**: temperature/humidity/pressure/co2, units, highAlarm, lowAlarm, alarmState
- **Alarm Chip**: alarmActive, alarmCount, acknowledged
- **Filter**: pressureDrop, dpAlarmHigh, dpWarning, filterStatus
- **Heater**: status, capacity, outputKW
- **Coils**: valvePosition, supplyTemp, returnTemp, airTempOut, active
- **Compressor**: status, alarmState, loadPercent, runtime
- **Motor**: status, speed, current, alarmState

See individual widget files for complete variable documentation.

## 🤝 Contributing

Contributions are welcome! To add new widgets or improve existing ones:

1. Fork the repository
2. Create a feature branch
3. Follow the widget structure and best practices
4. Test your widget in FUXA
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Inspired by [FUXA-SVG-Widgets](https://github.com/frangoteam/FUXA-SVG-Widgets)
- Built for the [FUXA SCADA platform](https://github.com/frangoteam/FUXA)
- Designed for building automation and BMS applications

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review the FUXA documentation

## 🗺️ Roadmap

Future enhancements:
- [ ] Additional widget categories (Electrical, Plumbing, etc.)
- [ ] Light theme variants
- [ ] Multi-language label support
- [ ] Configuration wizards
- [ ] Widget preview gallery
- [ ] Online widget designer
- [ ] More animation options
- [ ] Touch-optimized controls
- [ ] Accessibility improvements

---

**Version**: 1.0.0
**Last Updated**: 2025-10-09
**Total Widgets**: 82
**Categories**: 10

Made with ❤️ for the Building Automation community