numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
odd_numbers = [x for x in sorted_numbers if x % 2 != 0]
print(odd_numbers)