day_number = int(input("What is the number? "))

if day_number == 0:
    print('Sunday')
elif day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
else:
    print("This is not a valid number. Please choose a number between 0 and 6")

# List version

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
if 0 <= day_number <=6:
    print(days[day_number])
else:
    print("this is not a valid number")
