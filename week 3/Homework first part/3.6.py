numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for grade in numbers:
    if grade >= 75:
        print("First")
    elif 70 <= grade < 75:
        print("Upper Second")
    elif 60 <= grade < 70:
        print("Second")
    elif 50 <= grade < 60:
        print("Third")
    elif 45 <= grade < 50:
        print("F1 Supp")
    elif 40 <= grade < 45:
        print("F2")
    elif grade < 40:
        print("F3")
    else:
        print("Give a valid number between 0 and 100")
