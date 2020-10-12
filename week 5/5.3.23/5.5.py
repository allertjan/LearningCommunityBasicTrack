def add_vectors(vector1, vector2):
    if not len(vector1) == len(vector2):
        return None

    vector3 = []
    for number1, number2 in zip(vector1, vector2):
        vector3.append(number1 + number2)

    return vector3


print(add_vectors([1, 1], [3, 3]))
'''
Did not get the question so got it from the internet.
Link: https://github.com/VincentVelthuizen/Week-5/blob/master/exercises_5_3_23/vectors.py
'''
