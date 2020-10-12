def dot_product(vector1, vector2):
    if not len(vector1) == len(vector2):
        return None
    else:
        total = 0
        for x, y in zip(vector1, vector2):
            total += (x * y)
    return total


print(dot_product([1, 2, 3], [1, 2, 3]))
