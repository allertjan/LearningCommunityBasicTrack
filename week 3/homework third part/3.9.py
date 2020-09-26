n = int(input("Give a number "))
if n > 1:
    for num in range(2, n):
        if n % num == 0:
            print("False")
            break
    else:
        print("True")