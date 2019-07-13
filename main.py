import time
import turtle
from menu import Menu
from settings import Settings

# Instantiate screen and register all image assets
screen = turtle.Screen()
screen.setup(800, 1000)
screen.bgpic("backround.gif")
screen.addshape("play.button.gif")
screen.addshape("realstage.gif")
screen.addshape("realgreen.gif")
screen.addshape("realblack_stage.gif")
screen.addshape("real_blue_ken.gif")
screen.addshape("real_green_ken.gif")
screen.addshape("real_red_ken.gif")
screen.addshape("star.gif")

screen.tracer(0) # Only update screen after screen.update()

# Create the two menues (hidden by default)
menu = Menu()
settings = Settings()

# Default game options
stage = "stage1"
player_left = "blue"
player_right = "red"

# Main play button function
def f_play_button(x, y):
    menu.hide()
    settings.show()
    screen.update()
menu.play_button.onclick(f_play_button)

# All the stage button functions
def f_stage1(x,y):
    global stage
    settings.stage_star.goto(settings.stage1.pos())
    settings.stage_star.st()
    stage = "stage1"
    screen.update()
settings.stage1.onclick(f_stage1)

def f_stage2(x,y):
    global stage
    settings.stage_star.goto(settings.stage2.pos())
    settings.stage_star.st()
    stage = "stage2"
    screen.update()
settings.stage2.onclick(f_stage2)

def f_stage3(x,y):
    global stage
    settings.stage_star.goto(settings.stage3.pos())
    settings.stage_star.st()
    stage = "stage3"
    screen.update()
settings.stage3.onclick(f_stage3)

# Left color select button functions
def f_ken_blue_left(x, y):
    global player_left
    settings.left_star.goto(settings.ken_blue_left.pos())
    settings.left_star.st()
    player_left = "blue"
    screen.update()
settings.ken_blue_left.onclick(f_ken_blue_left)

def f_ken_red_left(x, y):
    global player_left
    settings.left_star.goto(settings.ken_red_left.pos())
    settings.left_star.st()
    player_left = "red"
    screen.update()
settings.ken_red_left.onclick(f_ken_red_left)

def f_ken_green_left(x, y):
    global player_left 
    settings.left_star.goto(settings.ken_green_left.pos())
    settings.left_star.st()
    player_left = "green"
    screen.update()
settings.ken_green_left.onclick(f_ken_green_left)

# Right color selct button functions
def f_ken_blue_right(x, y):
    global player_right
    settings.right_star.goto(settings.ken_blue_right.pos())
    settings.right_star.st()
    player_right = "blue"
    screen.update()
settings.ken_blue_right.onclick(f_ken_blue_right)

def f_ken_red_right(x, y):
    global player_right
    settings.right_star.goto(settings.ken_red_right.pos())
    settings.right_star.st()
    player_right = "red"
    screen.update()
settings.ken_red_right.onclick(f_ken_red_right)

def f_ken_green_right(x, y):
    global player_right
    settings.right_star.goto(settings.ken_green_right.pos())
    settings.right_star.st()
    player_right = "green"
    screen.update()
settings.ken_green_right.onclick(f_ken_green_right)

#settings.show()
menu.show() # Show the main menu first
screen.update()
turtle.mainloop()