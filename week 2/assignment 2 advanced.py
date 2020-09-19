import math

distance = float(input("What is the distance to the destination? "))
print("The transportation mode options are: Car,Bike and Walking")
transportation = str.lower(input("Which transportation mode will you be using?"))
if transportation == "car":
    car_speed = float(input("What will be your average speed? "))
    time_hours = (distance//car_speed)
    rest_hours = (distance % car_speed)
    time_minutes = (rest_hours//(car_speed/60))
    rest_minutes = (rest_hours % (car_speed/60))
    time_seconds = math.ceil((rest_minutes/(car_speed/3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")
elif transportation == "bike":
    bike_speed = float(input("What will be your average speed? "))
    time_hours = (distance // bike_speed)
    rest_hours = (distance % bike_speed)
    time_minutes = (rest_hours // (bike_speed / 60))
    rest_minutes = (rest_hours % (bike_speed / 60))
    time_seconds = math.ceil((rest_minutes / (bike_speed / 3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")
elif transportation == "walking":
    walking_speed = float(input("What will be your average speed? "))
    time_hours = (distance // walking_speed)
    rest_hours = (distance % walking_speed)
    time_minutes = (rest_hours // (walking_speed / 60))
    rest_minutes = (rest_hours % (walking_speed / 60))
    time_seconds = math.ceil((rest_minutes / (walking_speed / 3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")
else:
    print("Please select one out of the following transportation modes: Car,Bike or Walking")
