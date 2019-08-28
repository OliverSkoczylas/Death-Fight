import turtle
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

KEYS = ["w", "a", "s", "d", "Up", "Down", "Left", "Right", "space"]
keys = {}
for key in KEYS:
    keys[key] = Key(key)

class Player(animations.Sprite):
    """
    Image naming template: name0b.gif, name1b.gif, name2b.gif
    State naming template: name, name_r
    States: duck_down, duck_up, idle, jump_up, jump_down, move_right, moveeft, punch
    """
    def __init__(self, direction, color):
        super(Player, self).__init__()
        self.speed = 10
        delay = 101
        path = "sprites/" + color + '/' + ('left/' if direction is 'left' else 'right/')
        
        # Examples
        # root = sprites/red/left
        # file = idle_01.gif
        #for root, _, files in os.walk("sprites"):
            

        self.add_state('duck_down', delay, [path + 'duck_down_01.gif', path + 'duck_down_02.gif', path + 'duck_down_03.gif'])
        self.add_state('duck_up', delay, [path + 'duck_up_01.gif', path + 'duck_up_02.gif', path + 'duck_up_03.gif'])                               
        self.add_state('punch' , delay, [path + 'punch_01.gif' , path + 'punch_02.gif' , path + 'punch_03.gif'])
        self.add_state('move' , delay, [path + 'move_01.gif' , path + 'move_02.gif' , path + 'move_03.gif'])
        self.add_state('jump' , delay, [path + 'jump_01.gif' , path + 'jump_02.gif' , path + 'jump_03.gif'])
        self.add_state('idle', delay, [path + 'idle_01.gif', path + 'idle_02.gif', path + 'idle_03.gif'])
        self.set_state('idle')

        """
        self.controls = {
            "d" : self.forward,
            "a" : self.back,
        }
        """

    def forward(self):
        super().forward(1)
        self.set_state('move')

    def back(self):
        super().back(1)
        
    def update(self):
        if keys["d"]:
            self.forward()
        if keys["a"]:
            self.back()
        super().update()

class Game:
    """
    Sprite example declaration

    shelly = animations.Sprite()
    shelly.add_state('idle', 101, ['idle02.gif', 'idle03.gif', 'idle03.gif'])
    shelly.set_state('idle')
    """

    def __init__(self, player_left_color, player_right_color):
        self.player_left = Player('left', player_left_color)        
        self.player_right = Player('right', player_right_color)
        self.player_left.penup()
        self.player_right.penup()
        self.player_left.goto(-150,0)
        self.player_right.goto(150,0)

        screen = self.player_left.getscreen()

        for key in KEYS:
            key = keys[key]
            screen.onkeypress(key.toggle, key.key)
            screen.onkey(key.toggle, key.key)

        screen.listen()

        while True:
            screen.update()
            self.player_left.update()
