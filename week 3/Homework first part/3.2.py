days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
start_number = int(input("What is the number of the day you are leaving? "))
stay_number = int(input("For how many day's are you gone?   "))
final_number = int(start_number + (stay_number % 7))
print(days_of_the_week[final_number])
