def readposint():
    number = input("Type a number")
    try:
        number = int(number)
    except ValueError:
        return -1
    else:
        return number >= 0


print(readposint())