import numpy as np
from numpy import random

class StatisticalAnalyzer:
    @staticmethod
    def calculate_percentile(data, percentile):
        return np.percentile(data, percentile)

    @staticmethod
    def calculate_mean(data):
        return np.mean(data)

    @staticmethod
    def calculate_median(data):
        return np.median(data)

    @staticmethod
    def calculate_variance(data):
        return np.var(data)

    @staticmethod
    def calculate_std_deviation(data):
        return np.std(data)

    @staticmethod
    def calculate_correlation(data1, data2):
        return np.corrcoef(data1, data2)[0, 1]

if __name__ == "__main__":
    ask = input("Do you want to input your own arrays? (yes/no): ").strip().lower()
    
    if ask == "yes":
        print("Note: Arrays length cannot be greater than 100")
        
        # Get input strings
        array1_input = input("Enter the first array elements separated by commas: ").strip()
        array2_input = input("Enter the second array elements separated by commas: ").strip()
        percentile_input = input("Enter the percentile to calculate (0-100): ").strip()
        
        # Validate empty inputs
        if not array1_input or not array2_input:
            print("Error: Arrays cannot be empty.")
            exit()
        
        # Validate percentile is a number
        try:
            percentile_value = int(percentile_input)
            if percentile_value < 0 or percentile_value > 100:
                print("Error: Percentile must be between 0 and 100.")
                exit()
        except ValueError:
            print("Error: Percentile must be a valid integer.")
            exit()
        
        # Try to convert arrays
        try:
            array1 = np.array([int(x.strip()) for x in array1_input.split(',')])
            array2 = np.array([int(x.strip()) for x in array2_input.split(',')])
        except ValueError:
            print("Error: Please enter only integer values separated by commas.")
            exit()
        
        # Validate array lengths
        if len(array1) > 100 or len(array2) > 100:
            print("Error: Array length cannot be greater than 100.")
            exit()
        
        if len(array1) != len(array2):
            print("Error: Both arrays must have the same length for correlation analysis.")
            exit()
            
    elif ask == "no":
        array1 = random.randint(1, 100, size=50)
        array2 = random.randint(1, 100, size=50)
        percentile_value = 50
        print("Generated random arrays of size 50")
        print(f"Using default percentile: {percentile_value}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        exit()
    
    # Display arrays
    print("\nArray 1:", array1)
    print("Array 2:", array2)
    
    # Calculate and display statistics
    print(f"\n--- Statistics for Array 1 and Array 2 ---")
    print(f"{percentile_value}th Percentile of Array 1: {StatisticalAnalyzer.calculate_percentile(array1, percentile_value)}")
    print(f"{percentile_value}th Percentile of Array 2: {StatisticalAnalyzer.calculate_percentile(array2, percentile_value)}")
    print(f"Mean of array 1: {StatisticalAnalyzer.calculate_mean(array1)}")
    print(f"Mean of array 2: {StatisticalAnalyzer.calculate_mean(array2)}")
    print(f"Median of array 1: {StatisticalAnalyzer.calculate_median(array1)}")
    print(f"Median of array 2: {StatisticalAnalyzer.calculate_median(array2)}")
    print(f"Variance of array 1: {StatisticalAnalyzer.calculate_variance(array1)}")
    print(f"Variance of array 2: {StatisticalAnalyzer.calculate_variance(array2)}")
    print(f"Standard Deviation of array 1: {StatisticalAnalyzer.calculate_std_deviation(array1)}")
    print(f"Standard Deviation of array 2: {StatisticalAnalyzer.calculate_std_deviation(array2)}")
    print(f"\nCorrelation between Array 1 and Array 2: {StatisticalAnalyzer.calculate_correlation(array1, array2)}")