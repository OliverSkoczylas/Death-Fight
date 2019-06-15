import turtle




class Settings:
  def __init__(self):
    self.map1 = turtle.Turtle()
    self.map1.penup()
    self.map1.shape("realstage.gif")
    self.map1.goto(-250,150)
    
    
    self.writer_map1 = turtle.Turtle()
    self.writer_map1.penup()
    self.writer_map1.goto(-323,200)
    self.writer_map1.hideturtle()
   
   
   
   
    self.map2 = turtle.Turtle()
    self.map2.penup()
    self.map2.shape("realgreen.gif")
    self.map2.goto(-25,125)  
    
    
    self.writer_map2 = turtle.Turtle()
    self.writer_map2.penup()
    self.writer_map2.goto(-100,200)
    self.writer_map2.hideturtle()
    
    
    
    self.map3 = turtle.Turtle()
    self.map3.penup()
    self.map3.shape("realblack_stage.gif")
    self.map3.goto(220,138)  
    
    
    self.writer_map3 = turtle.Turtle()
    self.writer_map3.penup()
    self.writer_map3.goto(120,200)
    self.writer_map3.hideturtle()
    
    
    self.writer_left = turtle.Turtle()
    self.writer_left.penup()
    self.writer_left.goto(-360, 20)
    self.writer_left.hideturtle()
    
    
    
    self.writer_right = turtle.Turtle()
    self.writer_right.penup()
    self.writer_right.goto(45, 20)
    self.writer_right.hideturtle()
    
    
    
    ken_blue_left = turtle.Turtle()
    ken_blue_left.penup()
    ken_blue_left.shape("real_blue_ken.gif")
    ken_blue_left.goto(-290,-50)
    
    ken_red_left = turtle.Turtle()
    ken_red_left.penup()
    ken_red_left.shape("real_red_ken.gif")
    ken_red_left.goto(-110,-50)
    
    ken_green_left = turtle.Turtle()
    ken_green_left.penup()
    ken_green_left.shape("real_green_ken.gif")
    ken_green_left.goto(-170, -90)
     
    ken_blue_right = turtle.Turtle()
    ken_blue_right.shape("real_blue_ken.gif")
    
    ken_red_right = turtle.Turtle()
    ken_red_right.shape("real_red_ken.gif")
    
    
    ken_green_right = turtle.Turtle()
    ken_green_right.shape("real_green_ken.gif")
    
    
    
    
    
    
    
    
    
    
    
    
    self.hide()   
  
  
  
  
  def show(self):

    self.map1.showturtle()  
    self.map2.showturtle() 
    self.map3.showturtle() 
    self.writer_map1.write("Map 1", True, font=("arial", 40, "normal"))
    self.writer_map2.write("Map 2", True, font=("arial", 40, "normal"))
    self.writer_map3.write("Map 3", True, font=("arial", 40, "normal"))
    self.writer_left.write("Left Character Color", True, font=("arial", 25, "normal"))
    self.writer_right.write("Right Character Color", True, font=("arial", 25, "normal"))
  
  def hide(self):
   
    self.map1.hideturtle()
    self.map2.hideturtle()
    self.map3.hideturtle()
    self.writer_map1.clear()
    self.writer_map2.clear()
    self.writer_map3.clear()
    self.writer_left.clear()
    self.writer_right.clear()
    
    