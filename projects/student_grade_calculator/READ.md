# Grade Calculator

## Description
A Python-based grade calculator that processes student score data and computes essential statistical metrics. The application calculates mean scores, median values, standard deviations, and identifies top-performing students from an array of test scores.

## Features
- **Mean Calculation**: Computes the average score for each student across all tests
- **Median Calculation**: Determines the middle value of each student's score distribution
- **Standard Deviation**: Calculates the dispersion of scores to measure consistency
- **Top Performer Identification**: Identifies the highest-performing student based on mean scores

## Requirements
- Python 3.10 or higher
- NumPy library

## Installation

1. Ensure Python 3.10+ is installed on your system
2. Install the required NumPy library:

```bash
pip install numpy
```

## Usage

1. Clone or download this repository
2. Navigate to the project directory
3. Run the calculator:

```bash
python grade_calculator.py
```

The program will process the predefined student data and output statistical analyses for each student.

## Data Structure

The calculator expects student data in the following format:

```python
students = [
    {"name": "StudentName", "scores": [score1, score2, score3, ...]},
    # Add more students as needed
]
```

## Sample Output

```
Alice, average: 86.60
Bob, average: 80.40
Charlie, average: 97.20
Diana, average: 71.00
Eve, average: 89.60
Frank, average: 81.60
Grace, average: 91.20
Henry, average: 76.00
Iris, average: 97.00
Jack, average: 85.20

Alice, median: 88.00
Bob, median: 81.00
Charlie, median: 97.00
Diana, median: 71.00
Eve, median: 89.00
Frank, median: 82.00
Grace, median: 91.00
Henry, median: 76.00
Iris, median: 97.00
Jack, median: 85.00

Alice, standard deviation: 4.88
Bob, standard deviation: 2.73
Charlie, standard deviation: 1.72
Diana, standard deviation: 2.00
Eve, standard deviation: 2.15
Frank, standard deviation: 2.42
Grace, standard deviation: 1.72
Henry, standard deviation: 2.00
Iris, standard deviation: 1.41
Jack, standard deviation: 1.72

Topper: Charlie with mean score: 97.20
```

## Future Enhancements
- Separate calculation logic from display formatting
- Support for multiple top performers and tie-breaking
- Implementation of sample vs. population standard deviation options
- CSV/JSON file import/export capabilities
- Grade distribution visualization
- Percentile ranking system
- Letter grade assignment (A, B, C, D, F)
- Class-wide statistical analysis
- Input validation and error handling
- Interactive command-line interface

## Technical Notes
- The calculator currently uses NumPy's default population standard deviation (`np.std()`)
- Student data is stored as a list of dictionaries for easy manipulation
- Statistical calculations are performed using NumPy for efficiency and accuracy

## License
This project is open source and available for educational purposes.

## Author:
 https://github.com/Raj56468

---

**Note**: This is a learning project designed to demonstrate fundamental statistical calculations and Python programming concepts.