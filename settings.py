import turtle




class Settings:
  def __init__(self):
    self.stage1 = turtle.Turtle()
    self.stage1.penup()
    self.stage1.shape("realstage.gif")
    self.stage1.goto(-250,120)
    
    
    self.writer_stage1 = turtle.Turtle()
    self.writer_stage1.penup()
    self.writer_stage1.goto(-340,150)
    self.writer_stage1.ht()
   
   
   
   
    self.stage2 = turtle.Turtle()
    self.stage2.penup()
    self.stage2.shape("realgreen.gif")
    self.stage2.goto(-25,90)  
    
    
    self.writer_stage2 = turtle.Turtle()
    self.writer_stage2.penup()
    self.writer_stage2.goto(-125,150)
    self.writer_stage2.ht()
    
    
    
    self.stage3 = turtle.Turtle()
    self.stage3.penup()
    self.stage3.shape("realblack_stage.gif")
    self.stage3.goto(220,100)  
    
    
    self.writer_stage3 = turtle.Turtle()
    self.writer_stage3.penup()
    self.writer_stage3.goto(120,150)
    self.writer_stage3.ht()
    
    self.writer_left = turtle.Turtle()
    self.writer_left.penup()
    self.writer_left.goto(-360, 20)
    self.writer_left.ht()
    
    self.writer_right = turtle.Turtle()
    self.writer_right.penup()
    self.writer_right.goto(20, 20)
    self.writer_right.ht()
    
    
    
    self.ken_blue_left = turtle.Turtle()
    self.ken_blue_left.penup()
    self.ken_blue_left.shape("real_blue_ken.gif")
    self.ken_blue_left.goto(-290,-50)
    
    self.ken_red_left = turtle.Turtle()
    self.ken_red_left.penup()
    self.ken_red_left.shape("real_red_ken.gif")
    self.ken_red_left.goto(-110,-50)
    
    self.ken_green_left = turtle.Turtle()
    self.ken_green_left.penup()
    self.ken_green_left.shape("real_green_ken.gif")
    self.ken_green_left.goto(-190, -190)
     
    
    
    self.ken_blue_right = turtle.Turtle()
    self.ken_blue_right.penup()
    self.ken_blue_right.shape("real_blue_ken.gif")
    self.ken_blue_right.goto(110, -50)
    
    self.ken_red_right = turtle.Turtle()
    self.ken_red_right.penup()
    self.ken_red_right.shape("real_red_ken.gif")
    self.ken_red_right.goto(299, -50)
    
    self.ken_green_right = turtle.Turtle()
    self.ken_green_right.penup()
    self.ken_green_right.shape("real_green_ken.gif")
    self.ken_green_right.goto(200, -190)
    
    
    #star to each section
    self.stage_star = turtle.Turtle()
    self.stage_star.penup()
    self.stage_star.shape("star.gif")
    self.stage_star.ht()
    self.stage_star.goto(self.stage1.pos())
    
    
    self.left_star = turtle.Turtle()
    self.left_star.penup()
    self.left_star.shape("star.gif")
    self.left_star.ht()
    self.left_star.goto(self.ken_blue_left.pos())
    
    
    self.right_star = turtle.Turtle()
    self.right_star.penup()
    self.right_star.shape("star.gif")
    self.right_star.ht()
    self.right_star.goto(self.ken_red_right.pos())
    
    
    #start button at the very bottom

    self.start_button = turtle.Turtle()
    self.start_button.penup()
    self.start_button.shape("start_button.gif")
    self.start_button.goto(0,-300)
    self.start_button.ht()
    
  
    
    
    
    
    
    
    
    
    
    
    self.hide()   
  
  
  
  
  def show(self):

    self.stage1.st()  
    self.stage2.st() 
    self.stage3.st() 
    self.writer_stage1.write("stage 1", True, font=("arial", 40, "normal"))
    self.writer_stage2.write("stage 2", True, font=("arial", 40, "normal"))
    self.writer_stage3.write("stage 3", True, font=("arial", 40, "normal"))
    self.writer_left.write("Left Character Color", True, font=("arial", 25, "normal"))
    self.writer_right.write("Right Character Color", True, font=("arial", 25, "normal"))
    self.ken_blue_left.st()
    self.ken_red_left.st()
    self.ken_green_left.st()
    self.ken_blue_right.st()
    self.ken_red_right.st()
    self.ken_green_right.st()
    self.right_star.st()
    self.stage_star.st()
    self.left_star.st()
    self.start_button.st() 

  def hide(self):
   
    self.stage1.ht()
    self.stage2.ht()
    self.stage3.ht()
    self.writer_stage1.clear()
    self.writer_stage2.clear()
    self.writer_stage3.clear()
    self.writer_left.clear()
    self.writer_right.clear()
    self.ken_blue_left.ht()
    self.ken_red_left.ht()
    self.ken_green_left.ht()
    self.ken_blue_right.ht()
    self.ken_red_right.ht()
    self.ken_green_right.ht()
    
    