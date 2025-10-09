# FUXA Integration Guide

This guide explains how to use the WBG Widgets with FUXA SCADA.

## Widget Format

All widgets have been converted to FUXA's standard format using the export variable system.

### Variable Naming Convention

FUXA uses prefixes to identify variable types:

| Prefix | Type | Example |
|--------|------|---------|
| `_pn_` | Numeric | `_pn_temperature`, `_pn_speed` |
| `_ps_` | String | `_ps_label`, `_ps_mode` |
| `_pb_` | Boolean | `_pb_enabled`, `_pb_alarm` |
| `_pc_` | Color | `_pc_statusColor` |

### Widget Structure

Every widget follows this structure:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <style>
      /* CSS styles */
    </style>
  </defs>

  <!-- SVG graphics elements -->

  <script><![CDATA[
//!export-start
let _pn_variable1 = 0;
let _pn_variable2 = 100;
let _ps_label = "Status";
//!export-end

function init() {
  update();
}

function update() {
  // Update visual elements based on variable values
}

function putValue(id, value) {
  // Handle incoming value updates from FUXA
  if (id === '_pn_variable1') {
    _pn_variable1 = Number(value) || 0;
    update();
  }
}

init();
]]></script>
</svg>
```

## Importing Widgets into FUXA

### Step 1: Import SVG File

1. Open FUXA in your browser
2. Go to **Editor** mode
3. Click **Graphics** → **SVG Library**
4. Click **Import SVG**
5. Select the widget file (e.g., `fan.svg`)
6. The widget will appear in your SVG library

### Step 2: Add to View

1. Create or open a view
2. Drag the widget from the SVG library onto the canvas
3. Resize and position as needed

### Step 3: Bind Variables

1. **Select the widget** on the canvas
2. Open the **Properties** panel (right side)
3. You'll see a list of all exported variables
4. For each variable:
   - Click the **binding icon** (⚡)
   - Select your **Device** (PLC, Modbus, BACnet, etc.)
   - Select the **Tag/Address** to bind to
   - Set the **Read/Write** mode as needed

## Example: Fan Widget

### Widget Variables

The fan widget (`primitives/fan.svg`) exports:

```javascript
//!export-start
let _pn_status = 0;      // 0=off, 1=on
let _pn_speed = 0;       // 0-100 (%)
let _pn_alarm = 0;       // 0=normal, 1=alarm
//!export-end
```

### Binding Example

Assume you have a PLC device named "PLC1" with these tags:
- `AHU1_SF_Run` - Supply fan run status (0/1)
- `AHU1_SF_Speed` - Supply fan speed (0-100)
- `AHU1_SF_Fault` - Supply fan fault (0/1)

**Bind the variables:**

| Widget Variable | Bind To | Mode |
|----------------|---------|------|
| `_pn_status` | `PLC1.AHU1_SF_Run` | Read |
| `_pn_speed` | `PLC1.AHU1_SF_Speed` | Read |
| `_pn_alarm` | `PLC1.AHU1_SF_Fault` | Read |

The fan widget will now:
- Rotate blades when `_pn_status = 1` and `_pn_speed > 0`
- Display the speed percentage
- Show green status when running normally
- Show red status when `_pn_alarm = 1`

## Example: Thermostat Widget

### Widget Variables

The thermostat widget (`hvac/thermostat-card.svg`) exports:

```javascript
//!export-start
let _pn_currentTemp = 72;
let _pn_setpoint = 72;
let _pn_mode = 0;        // 0=Off, 1=Heat, 2=Cool, 3=Auto
let _pn_fanMode = 0;     // 0=Auto, 1=On
//!export-end
```

### Binding Example with Read/Write

| Widget Variable | Bind To | Mode |
|----------------|---------|------|
| `_pn_currentTemp` | `PLC1.Zone1_SpaceTemp` | Read |
| `_pn_setpoint` | `PLC1.Zone1_Setpoint` | Read/Write |
| `_pn_mode` | `PLC1.Zone1_Mode` | Read/Write |
| `_pn_fanMode` | `PLC1.Zone1_FanMode` | Read/Write |

**Read/Write Mode** allows:
- The widget displays current values from the PLC
- Clicking buttons on the widget **writes back** to the PLC
- Setpoint can be adjusted with up/down arrows
- Mode can be changed by clicking mode buttons

## Example: Valve Widget

### Widget Variables

The analog valve widget (`primitives/valve-analog.svg`) exports:

```javascript
//!export-start
let _pn_position = 0;     // Commanded position 0-100
let _pn_command = 0;      // Optional command value
let _pn_feedback = 0;     // Actual position feedback
//!export-end
```

### Binding with Command and Feedback

| Widget Variable | Bind To | Mode |
|----------------|---------|------|
| `_pn_position` | `PLC1.CHW_Valve_Cmd` | Read |
| `_pn_feedback` | `PLC1.CHW_Valve_Pos` | Read |

The valve will:
- Display `_pn_feedback` position if > 0, otherwise `_pn_position`
- Animate the valve stem based on position
- Color-code the position indicator

## Widget Animation

Many widgets include automatic animations:

### Rotating Elements
- **Fans**: Blades rotate when running, speed varies with `_pn_speed`
- **Pumps**: Impeller rotates when `_pn_status = 1`
- **Motors**: Cooling fan spins when running
- **Compressors**: Indicator rotates during operation

### Flow Animations
- **Dampers**: Blades rotate from closed (0°) to open (90°)
- **Valves**: Stem rotates to show position
- **Coils**: Glow effect when active
- **Heat Exchangers**: Flow arrows animate

### Status Indicators
- **Alarms**: Pulsing red indicator when `_pn_alarm = 1`
- **LEDs**: Color changes based on status
- **Gauges**: Needle moves to show value

## Troubleshooting

### Widget Not Updating

1. **Check variable binding**: Ensure variables are bound to valid tags
2. **Check tag values**: Use FUXA's debug mode to verify tag values are changing
3. **Check console**: Open browser console (F12) for JavaScript errors

### Variables Not Visible in Properties

1. **Re-import the widget**: Delete from library and import again
2. **Check export markers**: Ensure variables are between `//!export-start` and `//!export-end`
3. **FUXA version**: Ensure you're using a recent version of FUXA

### Animation Not Working

1. **Check status variable**: Many animations require `_pn_status = 1`
2. **Check speed variable**: Rotation speed depends on `_pn_speed` value
3. **Browser compatibility**: Some animations use modern CSS features

### Values Not Writing Back to PLC

1. **Check binding mode**: Ensure variable is set to **Read/Write**, not just Read
2. **Check permissions**: Verify FUXA has write permissions to the device
3. **Check PLC**: Confirm the tag/register is writable

## Advanced Usage

### Customizing Widget Behavior

You can modify widget behavior by editing the SVG file:

1. Open the widget in a text editor
2. Locate the `//!export-start` section
3. Add new variables or modify existing ones
4. Update the `update()` function to use new variables
5. Update the `putValue()` function to handle new variables
6. Save and re-import into FUXA

### Creating Multi-Instance Views

To use multiple instances of the same widget:

1. Import the widget once
2. Drag multiple copies onto your view
3. Each instance can have different variable bindings
4. Example: Multiple fan widgets, each bound to different AHU supply fans

### Performance Considerations

- **Animation intervals**: Default is 50ms, can be increased to 100ms for lower CPU usage
- **Complex widgets**: Systems-level widgets (chiller plants, etc.) have more elements
- **Browser**: Chrome/Edge generally performs best with SVG animations

## Widget Categories and Use Cases

### Primitives
**Best for**: Building custom HVAC schematics
- Drag individual components (fans, valves, dampers, coils)
- Arrange to match your actual equipment
- Bind each component to its corresponding PLC point

### HVAC
**Best for**: Equipment-level monitoring
- Complete equipment representations
- Shows all key parameters in one widget
- Use in equipment views or dashboards

### Systems
**Best for**: Plant-level overviews
- Shows entire systems (chiller plant, boiler plant)
- Multiple pieces of equipment in context
- Use in central plant monitoring views

### Zones
**Best for**: Occupant-facing displays
- Space comfort monitoring
- Conference room booking/control
- Use in lobby displays or room tablets

### Utilities
**Best for**: Energy monitoring
- Metering and consumption tracking
- Power quality monitoring
- Use in energy management dashboards

### Controls
**Best for**: Operator interfaces
- Manual control panels
- Override controls
- Schedule management

### Indicators
**Best for**: Status displays
- Gauge displays for key metrics
- Alarm banners
- Trend visualization

## Support

For issues or questions:
- Check the main [README.md](README.md)
- Review widget source code (look for `//!export-start` section)
- Consult [FUXA documentation](https://github.com/frangoteam/FUXA)
- Open an issue on GitHub

## Version Information

**Widget Library Version**: 1.0.0
**FUXA Compatibility**: FUXA v1.1.0+
**Last Updated**: 2025-10-09
