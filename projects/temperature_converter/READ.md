# Temperature Converter

A NumPy-based batch temperature converter that efficiently handles array operations for converting between Celsius, Fahrenheit, and Kelvin scales.

## Features

- **Batch Processing**: Convert entire arrays of temperatures in a single operation
- **Multiple Conversions**: Supports all 6 conversion combinations
- **Input Validation**: Warns when temperatures fall below absolute zero
- **High Precision**: Results rounded to 2 decimal places
- **Verification Tests**: Built-in tests with known temperature values

## Installation
```bash
pip install numpy
```

## Usage
```python
import numpy as np
from temperature_converter import celsius_to_fahrenheit, celsius_to_kelvin

# Create an array of temperatures
temps = np.array([0, 25.5, 100, -40])

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(temps)
print(fahrenheit)  # Output: [ 32.   77.9 212.  -40. ]

# Convert Celsius to Kelvin
kelvin = celsius_to_kelvin(temps)
print(kelvin)  # Output: [273.15 298.65 373.15 233.15]
```

## Available Functions

| Function | Description |
|----------|-------------|
| `celsius_to_fahrenheit(arr)` | Convert Celsius to Fahrenheit |
| `fahrenheit_to_celsius(arr)` | Convert Fahrenheit to Celsius |
| `celsius_to_kelvin(arr)` | Convert Celsius to Kelvin |
| `kelvin_to_celsius(arr)` | Convert Kelvin to Celsius |
| `fahrenheit_to_kelvin(arr)` | Convert Fahrenheit to Kelvin |
| `kelvin_to_fahrenheit(arr)` | Convert Kelvin to Fahrenheit |

## Example Output
```
==============================================================
BATCH TEMPERATURE CONVERTER
==============================================================

Input Array (Celsius): [  0.   -273.15  100.    -40.     25.5 ]

--------------------------------------------------------------
CONVERSION RESULTS
--------------------------------------------------------------

1. Celsius to Fahrenheit:
   [ 32.   -459.67  212.    -40.     77.9 ]

2. Celsius to Kelvin:
   [273.15   0.   373.15 233.15 298.65]
```

## Temperature Reference Points

| Description | Celsius | Fahrenheit | Kelvin |
|-------------|---------|------------|--------|
| Absolute Zero | -273.15°C | -459.67°F | 0 K |
| Water Freezes | 0°C | 32°F | 273.15 K |
| Room Temperature | ~22°C | ~72°F | ~295 K |
| Body Temperature | 37°C | 98.6°F | 310.15 K |
| Water Boils | 100°C | 212°F | 373.15 K |

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: NumPy
- **Vectorization**: All operations leverage NumPy's vectorized computations for optimal performance
- **Precision**: Results rounded to 2 decimal places

## Conversion Formulas
```
Celsius to Fahrenheit:  F = (C × 9/5) + 32
Fahrenheit to Celsius:  C = (F - 32) × 5/9
Celsius to Kelvin:      K = C + 273.15
Kelvin to Celsius:      C = K - 273.15
```

## Testing

Run the built-in tests:
```bash
python temperature_converter.py
```

The script includes:
- Verification with known temperature values
- Round-trip conversion tests (C→F→C should equal original)
- Edge case validation (absolute zero handling)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

MIT License - feel free to use this code in your own projects.

## Author

Built with ❤️ using NumPy

---

**Note**: This converter validates against temperatures below absolute zero but allows the calculations to demonstrate edge cases. In real-world applications, you may want to raise exceptions for physically impossible temperatures.