# numbers.py
# Group ID: BHU/26/04

def mean(numbers):
    # Mean = Sum / Count
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def median(numbers):
    # Median = Middle number
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 1:
        return sorted_numbers[mid]
    else:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

def mode(numbers):
    # Mode = Number that appears most
    return max(set(numbers), key=numbers.count)

# Test the functions
my_list = [2, 4, 4, 6, 8, 10]

print("List:", my_list)
print("Mean:", mean(my_list))
print("Median:", median(my_list))
print("Mode:", mode(my_list))
