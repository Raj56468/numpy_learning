import numpy as np

def load_numbers(filepath):
    numbers = []
    with open(filepath, "r") as file:
        for line in file:
            for item in line.strip().split(","):
                item = item.strip()
                if item.lstrip("-").isdigit():  # handles negative numbers too
                    numbers.append(int(item))
    return np.array(numbers)

def even_odd_split(arr):
    even = arr[arr % 2 == 0]
    odd = arr[arr % 2 != 0]
    return even, odd

def sorted_numbers(arr):
    return np.sort(arr)

def calculate_statistics(arr):
    if len(arr) == 0:
        return None, None, None
    mean = np.mean(arr)
    median = np.median(arr)
    std_dev = np.std(arr)
    return mean, median, std_dev
    
def top_5_largest(arr):
    if len(arr) == 0:
        return np.array([])
    sorted_arr = np.sort(arr)
    return sorted_arr[-5:][::-1]  # return top 5 largest in descending order

def detect_outliers(arr):
    if len(arr) == 0:
        return np.array([])
    mean = np.mean(arr)
    std_dev = np.std(arr)
    threshold = 2 * std_dev
    outliers = arr[np.abs(arr - mean) > threshold]
    return outliers

def normalize_numbers_between_0_and_1(arr):
    if len(arr) == 0:
        return arr
    min_val = np.min(arr)
    max_val = np.max(arr)
    if min_val == max_val:
        return np.zeros_like(arr)  # all values are the same
    normalized = (arr - min_val) / (max_val - min_val)
    return normalized

if __name__ == "__main__":
    data = load_numbers('projects/company.txt')
    
    even_numbers, odd_numbers = even_odd_split(data)
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)

    sorted_nums = sorted_numbers(data)
    print("Sorted Numbers:", sorted_nums)

    mean, median, std_dev = calculate_statistics(data)
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")

    top_5 = top_5_largest(data)
    print("Top 5 Largest Numbers:", top_5)

    outliers = detect_outliers(data)
    print("Outliers:", outliers)

    normalized_data = normalize_numbers_between_0_and_1(data)
    print("Normalized Data:", normalized_data)