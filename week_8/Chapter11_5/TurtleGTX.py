import turtle


class TurtleGTX(turtle):

    def __init__(self):
        super().__init__()
        self.odo_meter = 0
        self.brokenn_down = False

    def jump(self, distance):
        pen = self.isdown()
        self.penup()
        self.forward(distance)
        if pen:
            self.pendown()

    def forward(self, distance: float):
        self.odo_meter += abs(distance)
        super().forward(distance)


