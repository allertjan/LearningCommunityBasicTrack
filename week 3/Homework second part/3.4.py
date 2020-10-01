import math

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0

for number in numbers:
    print(number, "The Square of the number is ", number ** 2)

for total_number in numbers:
    total += total_number

print(total)

print(sum(numbers))
product_numbers = math.prod(numbers)
print(product_numbers)
