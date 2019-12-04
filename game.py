import turtle
import os
import animations
import hitbox

class Key:
    def __init__(self, key):
        self.key = key
        self.is_pressed = False
    
    def toggle(self):
        if self.is_pressed:
            self.is_pressed = False
        else:
            self.is_pressed = True
    
    def __bool__(self):
        return self.is_pressed

class Controller:
    def __init__(self):
        self.keys = {}
        for key in KEYS:
            self.keys[key] = Key(key)
        
KEYS = ["w", "a", "s", "d", "Up", "Down", "Left", "Right", "space", "Shift_L", "Shift_R", "KP_0", 'Control_R', 'Escape']
controller = Controller()

class Player(animations.Sprite):
    """
    Image naming template: name0b.gif, name1b.gif, name2b.gif
    State naming template: name, name_r
    States: duck_down, duck_up, idle, jump_up, jump_down, move_right, moveeft, punch
    """
    def __init__(self, direction, color, ground_y):
        super(Player, self).__init__()
        self.direction = direction
        self.speed = 10
        self.health = 10
        self.ground_y = ground_y + 60
        self.body = hitbox.Hitbox(100, 116, self)
        self.fist = hitbox.Hitbox(38.66, 38.66, self, hitbox.Point(69.33 if direction == "left" else -69.33, 0))
        self.fist.is_active = False
        self.fist.hit = False
        self.is_jumping = False
        self.is_ducking = False
        self.is_punching = False
        self.horizontal_velocity = 1 if direction is 'right' else -1
        delay = 50
        path = "sprites/" + color + '/' + ('left/' if direction is 'left' else 'right/')

        duck_down = []
        duck_up = []
        punch = []
        move = []
        jump = []
        idle = []
        fall = []
        
        # Examples
        # root = sprites/red/left
        # file = idle_01.gif
        for root, _, files in os.walk(path):
            for file in files:
                if file.startswith("duck_down"):
                    duck_down.append(path + file)
                elif file.startswith("duck_up"):
                    duck_up.append(path + file)
                elif file.startswith("punch"):
                    punch.append(path + file)
                elif file.startswith("move"):
                    move.append(path + file)
                elif file.startswith("jump"):
                    jump.append(path + file)
                elif file.startswith("idle"):
                    idle.append(path + file)
                elif file.startswith('fall'):
                    fall.append(path + file)

        #puts the files in order
        
        duck_down.sort()        
        duck_up.sort()
        punch.sort()
        move.sort()
        jump.sort()
        idle.sort()
        fall.sort()

        self.add_state('duck_down', delay, duck_down, False)
        self.add_state('duck_up', delay, duck_up, False)                               
        self.add_state('punch' , delay, punch, False)
        self.add_state('move' , delay, move)
        self.add_state('jump' , delay, jump, False)
        self.add_state('fall' , delay, fall, False)
        self.add_state('idle', delay, idle)
        self.set_state('idle')
        

        if direction is 'left':
            self.right_key = 'a'
            self.left_key = 'd'
            self.punch_key = "space"
            self.jump_key = 'w'
            self.duck_key = 's'
        
        else:
            self.right_key = 'Right'
            self.left_key = 'Left'
            self.punch_key = 'Control_R'
            self.jump_key = "Up" 
            self.duck_key = "Down"

    def left(self):
        self.back(self.horizontal_velocity)
        self.set_state('move')

    def right(self):
        self.forward(self.horizontal_velocity)
        self.set_state('move')
        
    def update(self, other_fist):
        
        
        if self.is_jumping:
            self.sety(self.ycor() + self.velocity)
            if self.velocity <= 0:
                self.set_state("fall")
            if self.ycor() <= self.ground_y:
                self.is_jumping = False
            
            if controller.keys[self.left_key]:
                self.back(self.horizontal_velocity)
            elif controller.keys[self.right_key]:
                self.forward(self.horizontal_velocity)
            self.velocity -= .01
        
        elif self.is_ducking:
            ducking_is_done = False
            if not controller.keys[self.duck_key] and self.states["duck_down"].is_done:
                ducking_is_done = True
                self.set_state('duck_up')
            if ducking_is_done and self.states['duck_up'].is_done:
                self.is_ducking = False

        
        elif self.is_punching:
            self.fist.is_active = True
            if self.states["punch"].is_done:
                self.fist.is_active = False
                self.is_punching = False    
                self.fist.hit = False

        else:
           
            if self.body.is_colliding(other_fist) and other_fist.is_active and not other_fist.hit:
                other_fist.hit = True
                self.health -= 1
                print(self.direction + ":" + str(self.health))
                

            if controller.keys[self.left_key]:
                self.left()
            elif controller.keys[self.right_key]:
                self.right()
            elif controller.keys[self.punch_key]:
                self.set_state('punch')
                self.is_punching = True
            elif controller.keys[self.jump_key]:
                self.set_state('jump')
                self.is_jumping = True
                self.velocity = 2
            elif controller.keys[self.duck_key]:
                self.set_state("duck_down")
                self.is_ducking = True
            else:
                self.set_state("idle")    
        super().update()

class Game:
    """
    Sprite example declaration

    shelly = animations.Sprite()
    shelly.add_state('idle', 101, ['idle02.gif', 'idle03.gif', 'idle03.gif'])
    shelly.set_state('idle')
    """

    def __init__(self, player_left_color, player_right_color):
        self.player_left = Player('left', player_left_color, -2)        
        self.player_right = Player('right', player_right_color, 0)
        self.player_left.penup()
        self.player_right.penup()
        self.player_left.goto(-150,0)
        self.player_right.goto(150,0)

        screen = self.player_right.getscreen()

        for key in KEYS:
            key = controller.keys[key]
            screen.onkeypress(key.toggle, key.key)
            screen.onkey(key.toggle, key.key)

        self.back_arrow = turtle.Turtle()
        self.back_arrow.penup()
        self.back_arrow.shape('back_arrow.gif')
        self.back_arrow.goto(-300, 700)
        
        self.writer = turtle.Turtle()
        self.writer.penup()
        self.writer.goto(20, 20)
        self.writer.ht()
        
        self.left_health = 10
        self.right_health = 10
            
        self.update_health()
            
        screen.listen()

        while True:
            screen.update()
            if controller.keys['Escape']:
                break
            self.player_right.update(self.player_left.fist)
            self.player_left.update(self.player_right.fist)
            hitbox.update()

            if self.left_health != self.player_left.health:
                self.update_health()

            if self.right_health != self.player_right.health:
                self.update_health()

    def update_health(self):
        self.writer.clear()
        self.writer.goto(-440, 315)
        self.writer.write(self.player_left.health, True, font=("arial", 40, "normal"))
        self.left_health = self.player_left.health
        self.writer.goto(440, 315)
        self.writer.write(self.player_right.health, True, font=("arial", 40, "normal"))
        self.right_health = self.player_right.health
