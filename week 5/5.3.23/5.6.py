def scalar(multiplier, vector):
    new_vector = []
    for number in vector:
        new_vector.append(vector[0] * multiplier)
    return new_vector


print(scalar(3, [1, 1]))

