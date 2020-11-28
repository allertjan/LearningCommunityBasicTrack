from week_8.Chapter11_3.MyTime import MyTime

time1 = MyTime(11, 20, 20)
time2 = MyTime(5, 20, 20)
object_time = MyTime(5, 9, 9)
print(time1)
print(time1.between(time2, object_time))
print(time1 > time2)
print(time1.increment(-1, 20, 20))
