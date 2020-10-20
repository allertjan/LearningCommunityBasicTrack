
def time_calculation(distance_to_travel, speed, extra_time1):
    calc_time_hours = (distance_to_travel // speed)
    rest_hours = (distance_to_travel % speed)
    calc_time_minutes = (rest_hours // (speed / 60))
    total_minutes = (calc_time_hours * 60) + calc_time_minutes + extra_time1
    total_xy = int((calc_time_hours * 60) + calc_time_minutes)
    time_hours = int(total_minutes // 60)
    time_minutes = int(total_minutes % 60)
    text = "The travel time will be " + str(time_hours) + " hours " + str(time_minutes) + " minutes"
    return {"x": total_xy, "y": text}


def minutes_to_time_conversion(minutes):
    time_hours = int(minutes // 60)
    time_minutes = int(minutes % 60)
    print("The travel time will be", time_hours, "hours", time_minutes, "minutes")


def end_calc_time(specific_dictionary, travel_distance, speed):
    if travel_distance in transportation_dictionary[specific_dictionary]:
        minutes_to_time_conversion(transportation_dictionary[specific_dictionary][travel_distance] + extra_time)
    else:
        print(time_calculation(travel_distance, speed, extra_time)["y"])
        transportation_dictionary[specific_dictionary][travel_distance] = time_calculation(travel_distance, speed,
                                                                                           extra_time)["x"]
# It still does not save it to the dictionary in the document however when using the debugger it does?


def request_run_again():
    global value
    while True:
        value = str.lower(input("Would you like to run the program again? (yes/no)"))
        if value in ("yes", "no"):
            break
        else:
            print("invalid output")


total_x = 0
value = ""
transportation_dictionary = {
    "car_dictionary": {
        "distance": "time(in minutes)",
        40: 30,
        80: 60,
        120: 90,
        160: 120,
        240: 180,
    },
    "bike_dictionary": {
        20: 60,
        40: 120,
    },
    "walking_dictionary": {
        5: 60,
        10: 120,
    }
}
while True:
    print("The transportation mode options are: Car,Bike and Walking. You can also choose your own type of"
          " transportation mode by typing \"new\"")
    transportation = str.lower(input("Which transportation mode will you be using?"))
    if transportation in ["new", "car", "bike", "walking"]:
        distance = int(input("What is the distance to your destination?"))
        extra_time = int(input("How many extra time do you expect you will need?(minutes)"))
        if transportation == "car":
            end_calc_time("car_dictionary", distance, 80)
            request_run_again()
            if value == "yes":
                continue
            else:
                exit()
        elif transportation == "new":
            speed_new_transportation_mode = int(input("What is the speed of the new transportation mode? Speed:"))
            print(time_calculation(distance, speed_new_transportation_mode, extra_time)["y"])
            request_run_again()
            if value == "yes":
                continue
            else:
                exit()
        elif transportation == "bike":
            end_calc_time("bike_dictionary", distance, 20)
            request_run_again()
            if value == "yes":
                continue
            else:
                exit()
        elif transportation == "walking":
            end_calc_time("walking_dictionary", distance, 5)
            request_run_again()
            if value == "yes":
                continue
            else:
                exit()
    elif transportation not in ["new", "car", "bike", "walking"]:
        print("You have probably made a typing error")
        request_run_again()
        if value == "yes":
            continue
        else:
            print("Goodbye")
            break
