class rectangle:

    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """" create an area"""
        surface = self.width * self.height
        return surface

    def perimeter(self):
        """" Calculate the perimeter"""
        whole_perimeter = 2 * self.width + 2 * self.height
        return whole_perimeter

    def flip(self):
        """ Flip the width and the height of the rectangle"""
        self.height, self.width = self.width, self.height
        return self.width, self.height

    def contains(self, x, y):
        value = True
        if not self.corner.x <= x < self.width and self.corner.y <= y < self.height:
            value = False
        return value


