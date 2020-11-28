class point:
    """ Creating points  """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        self.x = self.y * -1
        return self.x, self.y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def slope_from_origin(self):
        return self.y / self.x

    def get_line(self, x, y):
        a = int((y - self.y) / abs(x - self.x))
        b = int(self.y - self.x * a)
        return a, b

    def calc_middle_of_circle(self, x2, y2, x3, y3, x4, y4):
        x_values = (self.x, x2, x3, x4)
        x1, x2, x3, x4 = sorted(x_values)




