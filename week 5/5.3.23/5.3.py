a = [1, 2, 3]
b = a[:] # b takes the same values as a.
b[0] = 5 # 1 becomes 5 in b, a does not change

print(a, b)

