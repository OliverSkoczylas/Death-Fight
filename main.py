import time
import turtle
from menu import Menu
from settings import Settings

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



screen.tracer(0)


menu = Menu()
settings = Settings()


#main play button
def f_play_button(x, y):
    menu.hide()
    settings.show()
    screen.update()
menu.play_button.onclick(f_play_button)

#these are all the map buttons
def f_map1(x,y):
    settings.map_star.goto(settings.map1.pos())
    settings.map_star.showturtle()
    screen.update()
settings.map1.onclick(f_map1)

def f_map2(x,y):
    settings.map_star.goto(settings.map2.pos())
    settings.map_star.showturtle()
    screen.update()
settings.map2.onclick(f_map2)

def f_map3(x,y):
    settings.map_star.goto(settings.map3.pos())
    settings.map_star.showturtle()
    screen.update()
settings.map3.onclick(f_map3)

#left color select buttons

def f_ken_blue_left(x, y):
    settings.left_star.goto(settings.ken_blue_left.pos())
    settings.left_star.showturtle()
    screen.update()
settings.ken_blue_left.onclick(f_ken_blue_left)

def f_ken_red_left(x, y):
    settings.left_star.goto(settings.ken_red_left.pos())
    settings.left_star.showturtle()
    screen.update()
settings.ken_red_left.onclick(f_ken_red_left)

def f_ken_green_left(x, y):
    settings.left_star.goto(settings.ken_green_left.pos())
    settings.left_star.showturtle()
    screen.update()
settings.ken_green_left.onclick(f_ken_green_left)

#right color selct buttons

def f_ken_blue_right(x, y):
    settings.right_star.goto(settings.ken_blue_right.pos())
    settings.right_star.showturtle()
    screen.update()
settings.ken_blue_right.onclick(f_ken_blue_right)

def f_ken_red_right(x, y):
    settings.right_star.goto(settings.ken_red_right.pos())
    settings.right_star.showturtle()
    screen.update()
settings.ken_red_right.onclick(f_ken_red_right)

def f_ken_green_right(x, y):
    settings.right_star.goto(settings.ken_green_right.pos())
    settings.right_star.showturtle()
    screen.update()
settings.ken_green_right.onclick(f_ken_green_right)

#settings.show()
menu.show()
screen.update()
turtle.mainloop()