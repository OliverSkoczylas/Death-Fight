import turtle
import os
import animations

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
        
KEYS = ["w", "a", "s", "d", "Up", "Down", "Left", "Right", "space", "Shift_L", "Shift_R", "KP_0"]
controller = Controller()

class Player(animations.Sprite):
    """
    Image naming template: name0b.gif, name1b.gif, name2b.gif
    State naming template: name, name_r
    States: duck_down, duck_up, idle, jump_up, jump_down, move_right, moveeft, punch
    """
    def __init__(self, direction, color):
        super(Player, self).__init__()
        self.speed = 10
        delay = 50
        path = "sprites/" + color + '/' + ('left/' if direction is 'left' else 'right/')

        duck_down = []
        duck_up = []
        punch = []
        move = []
        jump = []
        idle = []
        
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

        duck_down.sort()        
        duck_up.sort()
        punch.sort()
        move.sort()
        jump.sort()
        idle.sort()

        self.add_state('duck_down', delay, duck_down)
        self.add_state('duck_up', delay, duck_up)                               
        self.add_state('punch' , delay, punch)
        self.add_state('move' , delay, move)
        self.add_state('jump' , delay, jump)
        self.add_state('idle', delay, idle)
        self.set_state('idle')

        if direction is 'left':
            self.back_key = 'a'
            self.forward_key = 'd'
            self.punch_key = "space"
            self.jump_key = 'w'
            self.duck_key = 's'
        
        else:
            self.back_key = 'Left'
            self.forward_key = 'Right'
            self.punch_key = "KP_0"
            self.jump_key = "Up" 
            self.duck_key = "Down"

    def forward(self):
        super().forward(1)
        self.set_state('move')

    def back(self):
        super().back(1)
        self.set_state('move')
        
    def update(self):
        if controller.keys[self.forward_key]:
            self.forward()
        elif controller.keys[self.back_key]:
            self.back()
        elif controller.keys[self.punch_key]:
            self.set_state('punch')
        elif  controller.keys[self.jump_key]:
            self.set_state('jump')        
        elif controller.keys[self.duck_key]:
            self.set_state("duck_down")
        
        
        
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
        #self.player_left = Player('left', player_left_color)        
        self.player_right = Player('right', player_right_color)
        #self.player_left.penup()
        self.player_right.penup()
        #self.player_left.goto(-150,0)
        self.player_right.goto(150,0)

        screen = self.player_right.getscreen()

        for key in KEYS:
            key = controller.keys[key]
            screen.onkeypress(key.toggle, key.key)
            screen.onkey(key.toggle, key.key)

        screen.listen()

        while True:
            screen.update()
            self.player_right.update()
