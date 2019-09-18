import turtle

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

class Hitbox(turtle.Turtle):
    def __init__(self, width, height, offset):
        self.width = width
        self.height = height
        self.offstet = offset

        
    def is_colliding(self, hitbox):
        

    def update(self):
        Point(self.xcor() - self.width / 2, self.ycor() - self.height / 2)