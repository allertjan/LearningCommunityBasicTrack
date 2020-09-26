odd_count = 0
sum_even_count = 0
negative_number_sum = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -5, -7]


for odd in numbers:
    if odd % 2 == 1:
        odd_count += 1

print("There are ", odd_count, "odd numbers")

for sum_even in numbers:
    if sum_even % 2 == 0:
        sum_even_count += sum_even
print("This is the sum of all the even numbers:", sum_even_count)

for negative_numbers in numbers:
    if negative_numbers < 0:
        negative_number_sum += negative_numbers
print("The sum of all negative numbers are:", negative_number_sum)


