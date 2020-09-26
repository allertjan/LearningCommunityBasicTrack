import math

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0

for number in numbers:
    print(number, "The Square of the number is ", number ** 2)

for total_number in numbers:
    total = sum(numbers)

print(total)

product_numbers = math.prod(numbers)
print(product_numbers)
