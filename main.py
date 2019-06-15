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

screen.tracer(0)




menu = Menu()
settings = Settings()

def f_play_button(x, y):
    menu.hide()
    settings.show()
    screen.update()

menu.play_button.onclick(f_play_button)


def f_map1(x, y):
    


settings.map1.onclick()





















#settings.show()
menu.show()

screen.update()

turtle.mainloop()