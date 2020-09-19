current_time = int(input("what is the time currently? "))
time_alarm = int(input("For how many hours do you want to set an alarm? "))
end_time_alarm = (current_time + time_alarm) % 24
print("The alarm goes of at", end_time_alarm)