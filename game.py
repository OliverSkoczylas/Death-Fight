import turtle
import animations

class Player(animations.Sprite):
    """
    Image naming template: name0b.gif, name1b.gif, name2b.gif
    State naming template: name_l, name_r
    States: duck_down, duck_up, idle, jump_up, jump_down, move_right, move_left, punch
    """
    def __init__(self, direction, color):
        super(Player, self).__init__()
        self.direction = direction
        delay = delay
        path = path + '' + color + '/'
        path_left = path + 'left/'
        path_right = path + 'right/'
        self.add_state('idle_l', delay, [path_left + 'idle0.gif', path_left + 'idle1.gif', path_left + 'idle2.gif'])
        self.add_state('duck_down_l', delay, [path_left + 'duck_down0.gif', path_left + 'duck_down1.gif', path_left + 'duck_down2.gif'])
        self.add_state('duck_up_l', delay , [path_left + 'duck_up0.gif', path_left + 'duck_up1.gif', path_left + 'duck_up2.gif'])                               ')
        self.add_state('punch_l' , delay , [path_left + 'punch0.gif' , path_left + 'punch1.gif' , path_left + 'punch2.gif'])
        self.add_state
        self.add_state



class Game:
    """
    Sprite example declaration

    shelly = animations.Sprite()
    shelly.add_state('idle', 100, ['idle01.gif', 'idle02.gif', 'idle03.gif'])
    shelly.set_state('idle')
    """

    def __init__(self, stage, player_left, player_right):
        self.player_left = animations.Sprite()
        self.
        
        self.player_right = animations.Sprite()
