side_a = float(input("Give size of first side   "))
side_b = float(input("Give size of second side  "))
side_c = float(input("Give size of third side   "))
max_error = 1e-7
sum_squares_a_b = (side_a ** 2) + (side_b ** 2)
sum_square_c = side_c ** 2
if abs(sum_squares_a_b - sum_square_c) < max_error:
    print("This is a right angled triangle")
else:
    print("This is not a right angled triangle")
