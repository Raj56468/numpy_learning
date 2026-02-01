import numpy as np

# Test array with various temperature values
arr = np.array([0, -273.15, 100, -40, 25.5])

def celsius_to_fahrenheit(arr):
    """Convert Celsius to Fahrenheit for array of temperatures.
    
    Formula: F = (C * 9/5) + 32
    
    Args:
        arr: NumPy array of temperatures in Celsius
    
    Returns:
        NumPy array of temperatures in Fahrenheit
    """
    arr = np.array(arr)
    if np.any(arr < -273.15):
        print("Warning: Temperature below absolute zero (-273.15°C) detected!")
    return np.round((arr * 9/5) + 32, 2)

def fahrenheit_to_celsius(arr):
    """Convert Fahrenheit to Celsius for array of temperatures.
    
    Formula: C = (F - 32) * 5/9
    
    Args:
        arr: NumPy array of temperatures in Fahrenheit
    
    Returns:
        NumPy array of temperatures in Celsius
    """
    arr = np.array(arr)
    if np.any(arr < -459.67):
        print("Warning: Temperature below absolute zero (-459.67°F) detected!")
    return np.round((arr - 32) * 5/9, 2)

def celsius_to_kelvin(arr):
    """Convert Celsius to Kelvin for array of temperatures.
    
    Formula: K = C + 273.15
    
    Args:
        arr: NumPy array of temperatures in Celsius
    
    Returns:
        NumPy array of temperatures in Kelvin
    """
    arr = np.array(arr)
    if np.any(arr < -273.15):
        print("Warning: Temperature below absolute zero (-273.15°C) detected!")
    return np.round(arr + 273.15, 2)

def kelvin_to_celsius(arr):
    """Convert Kelvin to Celsius for array of temperatures.
    
    Formula: C = K - 273.15
    
    Args:
        arr: NumPy array of temperatures in Kelvin
    
    Returns:
        NumPy array of temperatures in Celsius
    """
    arr = np.array(arr)
    if np.any(arr < 0):
        print("Warning: Temperature below absolute zero (0K) detected!")
    return np.round(arr - 273.15, 2)

def fahrenheit_to_kelvin(arr):
    """Convert Fahrenheit to Kelvin for array of temperatures.
    
    Combines fahrenheit_to_celsius() and celsius_to_kelvin()
    
    Args:
        arr: NumPy array of temperatures in Fahrenheit
    
    Returns:
        NumPy array of temperatures in Kelvin
    """
    arr = np.array(arr)
    return celsius_to_kelvin(fahrenheit_to_celsius(arr))

def kelvin_to_fahrenheit(arr):
    """Convert Kelvin to Fahrenheit for array of temperatures.
    
    Combines kelvin_to_celsius() and celsius_to_fahrenheit()
    
    Args:
        arr: NumPy array of temperatures in Kelvin
    
    Returns:
        NumPy array of temperatures in Fahrenheit
    """
    arr = np.array(arr)
    return celsius_to_fahrenheit(kelvin_to_celsius(arr))

def run_tests():
    """Run tests with known temperature conversion values."""
    print("=" * 60)
    print("VERIFICATION WITH KNOWN VALUES")
    print("=" * 60)
    
    # Test with known values
    test_celsius = np.array([0, 100, -40])
    expected_fahrenheit = np.array([32, 212, -40])
    expected_kelvin = np.array([273.15, 373.15, 233.15])
    
    print("\nTest Array (Celsius):", test_celsius)
    print("Expected Fahrenheit:", expected_fahrenheit)
    print("Actual Fahrenheit:  ", celsius_to_fahrenheit(test_celsius))
    print("Expected Kelvin:    ", expected_kelvin)
    print("Actual Kelvin:      ", celsius_to_kelvin(test_celsius))
    
    # Verify round-trip conversions
    print("\n" + "=" * 60)
    print("ROUND-TRIP CONVERSION TEST")
    print("=" * 60)
    original = np.array([25.5, 0, 100])
    print("\nOriginal Celsius:", original)
    converted = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
    print("After C→F→C:     ", converted)
    print("Difference:      ", np.round(original - converted, 10))

if __name__ == "__main__":
    print("=" * 60)
    print("BATCH TEMPERATURE CONVERTER")
    print("=" * 60)
    print("\nInput Array (Celsius):", arr)
    print("\n" + "-" * 60)
    print("CONVERSION RESULTS")
    print("-" * 60)
    
    print("\n1. Celsius to Fahrenheit:")
    print("  ", celsius_to_fahrenheit(arr))
    
    print("\n2. Fahrenheit to Celsius:")
    print("  ", fahrenheit_to_celsius(arr))
    
    print("\n3. Celsius to Kelvin:")
    print("  ", celsius_to_kelvin(arr))
    
    print("\n4. Kelvin to Celsius:")
    print("  ", kelvin_to_celsius(arr))
    
    print("\n5. Fahrenheit to Kelvin:")
    print("  ", fahrenheit_to_kelvin(arr))
    
    print("\n6. Kelvin to Fahrenheit:")
    print("  ", kelvin_to_fahrenheit(arr))
    
    # Run verification tests
    print("\n")
    run_tests()
    
    print("\n" + "=" * 60)
    print("ALL CONVERSIONS COMPLETE")
    print("=" * 60)