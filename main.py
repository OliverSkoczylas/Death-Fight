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


#settings.show()
menu.show()

screen.update()

turtle.mainloop()