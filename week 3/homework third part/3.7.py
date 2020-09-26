n = 25
approximation = n / 2
max_error = 1e-7

while True:
    better = (approximation + n / approximation) / 2
    if abs(better - approximation) < max_error:
        break
    print("Better", better)
    approximation = better
print(approximation)
