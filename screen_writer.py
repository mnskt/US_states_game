import turtle


ALIGN = 'center'
FONT = ('Verdana', 6, 'normal')


class ScreenWriter(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, x, y, answer_state):
        self.setpos(x, y)
        self.write(arg=answer_state, align=ALIGN, font=FONT)
