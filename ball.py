from turtle import Turtle


class TheBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.01

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.color("red")

    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_move *= -1
        self.color("green")

    def restart_game(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
        self.y_move *= -1

