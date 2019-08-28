import turtle

class Menu:
  def __init__(self):    
    self.play_button = turtle.Turtle()
    self.play_button.penup()
    self.play_button.goto(-10,0)
    self.play_button.setheading(180)
    self.play_button.shape("play.button.gif")
    
    self.hide()
    
  def show(self):
    self.play_button.st()
    
    self.play_button.st()
   
    
    
    
  def hide(self):
    self.play_button.ht()
    