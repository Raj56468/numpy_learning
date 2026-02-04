# Statistical Analyzer

A simple Python-based statistical analysis tool that computes various statistical measures for numerical datasets using NumPy.

## Features

This tool calculates the following statistics:

- **Percentiles** - Calculate any percentile (0-100) of your dataset
- **Mean** - Average value of the dataset
- **Median** - Middle value when data is sorted
- **Variance** - Measure of data spread
- **Standard Deviation** - Square root of variance
- **Correlation** - Pearson correlation coefficient between two datasets

## Requirements

- Python 3.x
- NumPy

## Installation

1. Clone or download this repository
2. Install NumPy if you haven't already:

```bash
pip install numpy
```

## Usage

Run the script:

```bash
python statistical_analyzer.py
```

### Interactive Mode

When you run the script, you'll be asked if you want to input your own arrays:

**Option 1: Input Your Own Data**
```
Do you want to input your own arrays? (yes/no): yes
Note: Arrays length cannot be greater than 100
Enter the first array elements separated by commas: 10,20,30,40,50
Enter the second array elements separated by commas: 15,25,35,45,55
Enter the percentile to calculate (0-100): 75
```

**Option 2: Use Random Data**
```
Do you want to input your own arrays? (yes/no): no
Generated random arrays of size 50
Using default percentile: 50
```

### Example Output

```
Array 1: [10 20 30 40 50]
Array 2: [15 25 35 45 55]

--- Statistics for Array 1 ---
75th Percentile: 40.0
Mean: 30.0
Median: 30.0
Variance: 200.0
Standard Deviation: 14.142135623730951

Correlation between Array 1 and Array 2: 1.0
```

## Input Validation

The program includes validation for:

- ✅ Non-numeric input (only integers accepted)
- ✅ Empty arrays
- ✅ Array length limits (max 100 elements)
- ✅ Mismatched array lengths for correlation
- ✅ Invalid percentile values (must be 0-100)
- ✅ Invalid yes/no responses

## Code Structure

```
StatisticalAnalyzer (Class)
├── calculate_percentile()
├── calculate_mean()
├── calculate_median()
├── calculate_variance()
├── calculate_std_deviation()
└── calculate_correlation()
```

All methods are static since they don't require instance state.

## Limitations

- Only accepts integer values (no floating-point numbers)
- Maximum array length of 100 elements
- Both arrays must be the same length for correlation analysis
- Only calculates Pearson correlation (not Spearman or other types)

## Future Enhancements

Potential improvements for this project:

- [ ] Support for floating-point numbers
- [ ] File input/output (CSV, TXT)
- [ ] Additional statistics (mode, range, IQR, skewness, kurtosis)
- [ ] Data visualization with matplotlib
- [ ] Support for multiple correlation types
- [ ] Batch processing of multiple datasets
- [ ] Export results to file
- [ ] Command-line arguments for non-interactive use

## Learning Objectives

This project was created to learn:

- NumPy array operations
- Statistical calculations
- Input validation and error handling
- Object-oriented programming with static methods
- User interaction and CLI design

## License

This project is open source and available for educational purposes.

## Author

Created as a learning project for statistical analysis with Python and NumPy.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

---

**Note:** This is a learning project and may not be suitable for production use. For professional statistical analysis, consider using libraries like SciPy, pandas, or statsmodels.