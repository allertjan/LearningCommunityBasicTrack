counter = 0
students = [
 ("John", ["CompSci", "Physics"]),
 ("Vusi", ["Maths", "CompSci", "Stats"]),
 ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
 ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
 ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
for name, subjects in students:
    if "CompSci" in subjects:
        counter += 1

print(counter)