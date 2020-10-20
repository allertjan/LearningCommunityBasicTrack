import math


def time_calculation(distance_to_travel, speed, extra_time1):
    time_hours = (distance_to_travel // speed)
    rest_hours = (distance_to_travel % speed)
    time_minutes = (rest_hours // (speed / 60)) + extra_time1
    rest_minutes = (rest_hours % (speed / 60))
    time_seconds = math.ceil((rest_minutes / (speed / 3600)))
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes", time_seconds, "seconds")


car_dictionary = {
    "distance": "time(in minutes)",
    80: 60,
    160: 120,
}
print("The transportation mode options are: Car,Bike and Walking. You can also add other type of transportation modes"
      " by typing \"add\"")
transportation = str.lower(input("Which transportation mode will you be using?"))
if transportation == "add":
    speed_new_transportation_mode = int(input("What is the speed of the new transportation mode? Speed:"))
distance = int(input("What is the distance to your destination?"))
extra_time = int(input("How many extra time do you expect you will need?(minutes)"))

if transportation == "car":
    if distance in car_dictionary:
        print("The travel time will be", str((car_dictionary[distance] + extra_time)), "minutes.")
    else:
        time_calculation(distance, 80, extra_time)
elif transportation == "add":
    time_calculation(distance, speed_new_transportation_mode, extra_time)
elif transportation == "bike":
    time_calculation(distance, 20, extra_time)
elif transportation == "walking":
    time_calculation(distance, 5, extra_time)
else:
    print("Please select one of the following transportation modes: Car,Bike,Walking or add")
