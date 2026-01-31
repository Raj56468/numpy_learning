import numpy as np

students = [
    {"name": "Alice", "scores": [85, 92, 78, 90, 88]},
    {"name": "Bob", "scores": [76, 84, 81, 79, 82]},
    {"name": "Charlie", "scores": [95, 98, 100, 97, 96]},
    {"name": "Diana", "scores": [68, 72, 70, 74, 71]},
    {"name": "Eve", "scores": [88, 91, 87, 93, 89]},
    {"name": "Frank", "scores": [82, 78, 85, 80, 83]},
    {"name": "Grace", "scores": [91, 89, 94, 90, 92]},
    {"name": "Henry", "scores": [73, 77, 75, 79, 76]},
    {"name": "Iris", "scores": [97, 95, 99, 98, 96]},
    {"name": "Jack", "scores": [84, 86, 83, 88, 85]}
]

def calculate_mean(students):
    for student in students:
        student['mean'] = np.mean(student['scores'])
        print(f'{student["name"]}, average: {student["mean"]:.2f}')

def calculate_median(students):
    for student in students:
        student['median'] = np.median(student['scores'])
        print(f'{student["name"]}, median: {student["median"]:.2f}')

def calculate_std_dev(students):
    for student in students:
        student['std_dev'] = np.std(student['scores'])
        print(f'{student["name"]}, standard deviation: {student["std_dev"]:.2f}')
    
def topper(students):
    top_student = max(students, key=lambda x: x['mean'])
    print(f'Topper: {top_student["name"]} with average:{top_student["mean"]:.2f}')

if __name__ == "__main__":
    calculate_mean(students)
    print()
    calculate_median(students)
    print()
    calculate_std_dev(students)
    print()
    topper(students)