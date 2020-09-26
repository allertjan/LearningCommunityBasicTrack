numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -5, -7]
total = 0
check_variable = 0
for all_number in numbers:
    if all_number % 2 == 1:
        total += all_number
    elif all_number % 2 == 0:
        if check_variable == 0:
            check_variable += 1
            continue
        else:
            total += all_number

print(total)


