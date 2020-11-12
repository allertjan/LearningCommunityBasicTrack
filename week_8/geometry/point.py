class point:
    """
    Point class represents and manipulates x and y coordinates.
    """
    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x * self.x + self.y * self.y) ** .5

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

