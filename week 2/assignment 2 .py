import math

distance = float(input("What is the distance to the destination? "))
print("The transportation mode options are: Car,Bike and Walking")
transportation = str.lower(input("Which transportation mode will you be using?"))
if transportation == "car":
    time_hours = (distance//80)
    rest_hours = (distance % 80)
    time_minutes = (rest_hours//(80/60))
    rest_minutes = (rest_hours % (80/60))
    time_seconds = math.ceil((rest_minutes/(80/3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")
elif transportation == "bike":
    time_hours = (distance // 20)
    rest_hours = (distance % 20)
    time_minutes = (rest_hours // (20 / 60))
    rest_minutes = (rest_hours % (20 / 60))
    time_seconds = math.ceil((rest_minutes / (20 / 3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")
elif transportation == "walking":
    time_hours = (distance // 5)
    rest_hours = (distance % 5)
    time_minutes = (rest_hours // (5 / 60))
    rest_minutes = (rest_hours % (5 / 60))
    time_seconds = math.ceil((rest_minutes / (5 / 3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")
else:
    print("Please select one out of the following transportation modes: Car,Bike or Walking")
