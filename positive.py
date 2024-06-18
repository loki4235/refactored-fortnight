def print_positive_numbers(numbers):
  positive_numbers = [num for num in numbers if num > 0]
  print(positive_numbers)

numbers = [12, -7, 5, 64, -14]
print_positive_numbers(numbers)
