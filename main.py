import numpy as np

def number_lab():
    even_numbers = []
    odd_numbers = []
    with open('projects/company.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.strip().split(',')
            for number in numbers:
                if number.isdigit():
                    num = int(number)
                    if num % 2 == 0:
                        even_numbers.append(num)
                    else:
                        odd_numbers.append(num)
    return np.array(even_numbers), np.array(odd_numbers)

def sorted_numbers():
    with open('projects/company.txt', 'r') as file:
        lines = file.readlines()
        all_numbers = []
        for line in lines:
            numbers = line.strip().split(',')
            for number in numbers:
                if number.isdigit():
                    all_numbers.append(int(number))
        all_numbers = np.array(all_numbers)
        all_numbers = np.sort(all_numbers)
    return all_numbers

def calculate_statistics():
    numbers = sorted_numbers()
    if len(numbers) == 0:
        return None, None, None
    mean = np.mean(numbers)
    median = np.median(numbers)
    std_dev = np.std(numbers)
    return mean, median, std_dev

if __name__ == "__main__":
    even_numbers, odd_numbers = number_lab()
    print("Even Numbers:", even_numbers)
    print("Odd Numbers:", odd_numbers)

    sorted_nums = sorted_numbers()
    print("Sorted Numbers:", sorted_nums)

    mean, median, std_dev = calculate_statistics()
    print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")
