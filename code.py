def find_odd_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = find_odd_even(numbers_list)

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")
