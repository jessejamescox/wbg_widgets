# Indicator/Display Widgets for FUXA

This directory contains 7 SVG-based indicator and display widgets with embedded JavaScript for real-time data visualization in FUXA SCADA systems.

## Widgets Overview

### 1. gauge-semicircle.svg
**180-degree semicircular gauge with needle indicator**

- **Features:**
  - Colored zones: Green (0-60%), Yellow (60-80%), Red (80-100%)
  - Animated needle rotation
  - Real-time value display with configurable decimals
  - Configurable min/max range and units
  - Scale markings at 0, 25, 50, 75, 100%

- **FUXA Methods:**
  ```javascript
  setValue(value)           // Update gauge value
  setOptions({              // Configure gauge
    min: 0,
    max: 100,
    unit: 'PSI',
    decimals: 1
  })
  getValue()                // Get current value
  ```

---

### 2. gauge-radial.svg
**Full 270-degree circular gauge with needle**

- **Features:**
  - Full radial display with 270-degree sweep
  - Colored arc zones (green/yellow/red)
  - Major and minor tick marks
  - Gradient needle with center hub
  - Smooth needle animation
  - Value display below gauge

- **FUXA Methods:**
  ```javascript
  setValue(value)           // Update gauge value
  setOptions({              // Configure gauge
    min: 0,
    max: 100,
    unit: 'RPM',
    decimals: 1
  })
  getValue()                // Get current value
  ```

---

### 3. gauge-horizontal.svg
**Horizontal bar gauge with gradient fill**

- **Features:**
  - Horizontal bar with color gradient (green→yellow→orange→red)
  - Fill animation
  - Position marker/pointer
  - Major and minor tick marks
  - Configurable title
  - Real-time value overlay

- **FUXA Methods:**
  ```javascript
  setValue(value)           // Update gauge value
  setOptions({              // Configure gauge
    min: 0,
    max: 100,
    unit: '%',
    decimals: 1,
    title: 'Level'
  })
  getValue()                // Get current value
  ```

---

### 4. trend-mini.svg
**Mini sparkline trend chart for recent history**

- **Features:**
  - Displays last 24 data points (configurable)
  - Sparkline style with area fill
  - Auto-scaling or fixed scale
  - Real-time statistics (Min/Max/Avg)
  - Grid background
  - Current value highlight dot
  - Smooth line interpolation

- **FUXA Methods:**
  ```javascript
  setValue(value)           // Add new data point
  setOptions({              // Configure chart
    maxPoints: 24,
    decimals: 1,
    unit: '°C',
    autoScale: true,
    minScale: 0,
    maxScale: 100
  })
  clearData()               // Clear all data points
  getValue()                // Get last value
  ```

---

### 5. status-led.svg
**Simple LED status indicator with multiple states**

- **Features:**
  - 5 states: OFF (0), OK/Green (1), WARNING/Yellow (2), ALARM/Red (3), RUNNING/Blue (4)
  - 3D LED effect with highlight
  - Optional blinking
  - Glow effect for active states
  - Configurable label
  - State name display

- **FUXA Methods:**
  ```javascript
  setValue(state)           // Set LED state (0-4)
  setOptions({              // Configure LED
    label: 'Pump Status',
    blink: true,
    blinkInterval: 500
  })
  getValue()                // Get current state
  ```

- **States:**
  - 0: OFF (gray)
  - 1: OK/Green
  - 2: WARNING/Yellow
  - 3: ALARM/Red
  - 4: RUNNING/Blue

---

### 6. alarm-banner.svg
**Scrolling alarm banner with priority indication**

- **Features:**
  - Priority levels: None (0), Low (1), Medium (2), High (3), Critical (4)
  - Color-coded priority bar
  - Auto-scrolling message (configurable speed)
  - Timestamp display
  - Acknowledge button
  - Alarm count badge
  - Bell icon with notification dot
  - Event emission on acknowledge

- **FUXA Methods:**
  ```javascript
  setValue({                // Set alarm (object or priority number)
    priority: 4,
    message: 'High temp alarm',
    timestamp: '2025-10-09 14:30:45',
    acknowledged: false,
    count: 3
  })
  setOptions({              // Configure banner
    scroll: true,
    scrollSpeed: 50,        // pixels per second
    message: 'Custom message',
    timestamp: '2025-10-09 14:30:45'
  })
  acknowledge()             // Acknowledge current alarm
  getValue()                // Get alarm object
  ```

- **Events:**
  - `alarm-acknowledged`: Fired when ACK button is clicked

---

### 7. mode-indicator.svg
**Operating mode display with animated status**

- **Features:**
  - 6 operating modes with unique icons and colors
  - Animated status dots for active modes
  - Glow effect
  - Mode-specific icons
  - Subtitle descriptions

- **FUXA Methods:**
  ```javascript
  setValue(mode)            // Set mode (0-5 or string name)
  setOptions({              // Configure indicator
    showStatus: true
  })
  getValue()                // Get current mode number
  getModeName()             // Get mode name string
  ```

- **Modes:**
  - 0: AUTO (green) - Automatic Operation
  - 1: MANUAL (blue) - Manual Control
  - 2: OFF (gray) - System Disabled
  - 3: ERROR (red) - Fault Condition
  - 4: MAINT (orange) - Maintenance Mode
  - 5: STANDBY (purple) - Ready to Start

---

## Integration with FUXA

### Basic Usage

1. **Import Widget:**
   - Upload SVG file to FUXA
   - Add to your HMI screen

2. **Bind Variable:**
   - Select widget
   - Bind to PLC tag or internal variable
   - Widget automatically updates via `setValue()`

3. **Configure Options:**
   - Use FUXA's property editor
   - Or call `setOptions()` via script

### Example FUXA Script

```javascript
// Update gauge
var gauge = document.getElementById('gauge-semicircle');
gauge.setValue(75.5);
gauge.setOptions({ min: 0, max: 150, unit: 'PSI' });

// Update trend chart
var trend = document.getElementById('trend-mini');
setInterval(function() {
  trend.setValue(getCurrentTemperature());
}, 1000);

// Update LED based on condition
var led = document.getElementById('status-led');
if (temperature > 80) {
  led.setValue(3); // Red alarm
} else if (temperature > 60) {
  led.setValue(2); // Yellow warning
} else {
  led.setValue(1); // Green OK
}

// Handle alarm acknowledgement
var banner = document.getElementById('alarm-banner');
banner.addEventListener('alarm-acknowledged', function(e) {
  console.log('Alarm acknowledged:', e.detail);
  // Send ACK to PLC
});
```

---

## Features Common to All Widgets

- **Real-time Updates:** All widgets respond immediately to value changes
- **FUXA Compatible:** Standard `setValue()`, `setOptions()`, `getValue()` interface
- **Configurable:** Extensive options for customization
- **Responsive:** SVG-based for scalability
- **Dark Theme:** Optimized for industrial HMI displays
- **No Dependencies:** Pure SVG + JavaScript, no external libraries

---

## File Sizes

- gauge-semicircle.svg: 4.3 KB
- gauge-radial.svg: 5.5 KB
- gauge-horizontal.svg: 5.2 KB
- trend-mini.svg: 7.1 KB
- status-led.svg: 6.7 KB
- alarm-banner.svg: 9.2 KB
- mode-indicator.svg: 7.8 KB

**Total: ~46 KB** for all 7 widgets

---

## Browser Compatibility

All widgets are tested and compatible with:
- Chrome/Edge (Chromium)
- Firefox
- Safari
- Embedded browsers in industrial HMI panels

---

## License

These widgets are part of the WBG Widgets collection for FUXA SCADA integration.
