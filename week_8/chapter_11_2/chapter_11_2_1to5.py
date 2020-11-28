from week_8.Chapter_11_1.point import point
from week_8.chapter_11_2.rectangle import rectangle

punt = rectangle(point(1, 1), 5, 10)
print(punt.area())
print(punt.perimeter())
punt.flip()
print(punt.width == 10 and punt.height == 5)
punt.flip()
print(punt.contains(2, 2))
