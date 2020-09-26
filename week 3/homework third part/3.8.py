number_amount = int(input("Which size n would you like? "))
triangle_number = 0
for i in range(1, (number_amount + 1)):
    triangle_number += i
    print(i,"   ", triangle_number)
    