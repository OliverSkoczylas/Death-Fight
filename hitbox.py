import turtle

hitboxes = []

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

class Hitbox(turtle.Turtle):
    def __init__(self, width, height, turtle=None, offset=Point(0, 0)):
        self.width = width
        self.height = height
        self.turtle = turtle
        self.offstet = offset
        self.update()
        hitboxes.append(self)
        
    def is_colliding(self, hitbox):
        if(self.l.x > hitbox.r.x or hitbox.l.x > self.r.x): 
            return False
        if(self.l.y < hitbox.r.y or hitbox.l.y < self.r.y): 
            return False
        return True

    def update(self):
        if self.turtle and self.offset:
            self.goto(self.turtle.xcor() + self.offset.x, self.turtle.ycor() + self.offset.y)
        self.l = Point(self.xcor() - self.width / 2, self.ycor() - self.height / 2)
        self.r = Point(self.xcor() + self.width / 2, self.ycor() + self.height / 2)

def update():
    for hitbox in hitboxes:
        hitbox.update()

if __name__ == "__main__":
    print("Running...")
    test = turtle.Turtle()
    test.shape("turtle")
    h1 = Hitbox(10, 10, test, Point(0, 0))
    h2 = Hitbox(10, 10)

    while True:
        h1.update()
        h2.update()
