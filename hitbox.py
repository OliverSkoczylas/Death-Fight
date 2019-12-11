import turtle
 
hitboxes = []
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)
 
class Hitbox(turtle.Turtle):
    def __init__(self, width, height, sprite=None, offset=Point(0, 0), draw=False):
        super().__init__()
        self.width = width
        self.height = height
        self.sprite = sprite
        self.offset = offset
        self.is_active = True
        self.draw = draw
        self.ht()
        self.penup()
        self.renderer = turtle.Turtle()
        self.renderer.shape('blank')
        self.update()
        hitboxes.append(self)

        
    def is_colliding(self, hitbox):
        #print("Me:\n\rL: %s, R: %s\nOther\n\rL: %s, R: %s\n" % (self.l, self.r, hitbox.l, hitbox.r))
        if(self.l.x > hitbox.r.x or hitbox.l.x > self.r.x):
            return False
        if(self.l.y < hitbox.r.y or hitbox.l.y < self.r.y):
            return False
        return self.is_active
 
    def update(self):
        if self.sprite and self.offset:
            self.goto(self.sprite.xcor() + self.offset.x, self.sprite.ycor() + self.offset.y)
        self.l = Point(self.xcor() - self.width / 2, self.ycor() + self.height / 2)
        self.r = Point(self.xcor() + self.width / 2, self.ycor() - self.height / 2)

        if self.draw and self.is_active:
            self.renderer.clear()
            self.renderer.goto(self.xcor() - self.width / 2, self.ycor() - self.height / 2)
            self.renderer.setheading(0)
            self.renderer.st()
            self.renderer.pendown()
            self.renderer.forward(self.width)
            self.renderer.left(90)
            self.renderer.forward(self.height)
            self.renderer.left(90)
            self.renderer.forward(self.width)
            self.renderer.left(90)
            self.renderer.forward(self.height)
            self.ht()
        else:
            self.renderer.clear()
            self.ht()
 
def update():
    for hitbox in hitboxes:
        hitbox.update()
 
if __name__ == "__main__":
    screen = turtle.Screen()
    print("Running...")
    indicator = turtle.Turtle()
    indicator.shape("turtle")
    indicator.color("red")
    indicator.ht()
    test = turtle.Turtle()
    test.shape("turtle")
    test.goto(100,100)
    h1 = Hitbox(20, 20, test, Point(0, 0))
    h2 = Hitbox(20, 20)
 
    def up():
        test.forward(10)
 
    def down():
        test.back(10)
 
    def left():
        test.left(10)
 
    def right():
        test.right(10)
 
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    screen.listen()
 
    while True:
        h1.update()
        h2.update()
        if h1.is_colliding(h2):
            indicator.st()
        else:
            indicator.ht()