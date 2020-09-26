side_a = float(input("Give the length of the first side"))
side_b = float(input("Give the length of the second side"))

power_side_a = side_a ** 2
power_side_b = side_b ** 2
length_side_c = (power_side_a + power_side_b) ** 0.5
print(length_side_c)