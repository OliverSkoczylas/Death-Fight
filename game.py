import turtle
import animations

class Player(animations.Sprite):
    """
    Image naming template: name0b.gif, name1b.gif, name2b.gif
    State naming template: name, name_r
    States: duck_down, duck_up, idle, jump_up, jump_down, move_right, moveeft, punch
    """
    def __init__(self, direction, color):
        super(Player, self).__init__()
        delay = 100
        path = path + '' + color + '/' + ('left/' if direction is 'left' else 'right/')
        self.add_state('duck_down', delay, [path + 'duck_down0.gif', path + 'duck_down1.gif', path + 'duck_down2.gif'])
        self.add_state('duck_up', delay, [path + 'duck_up0.gif', path + 'duck_up1.gif', path + 'duck_up2.gif'])                               ')
        self.add_state('punch' , delay, [path + 'punch0.gif' , path + 'punch1.gif' , path + 'punch2.gif'])
        self.add_state('move' , delay, [path + 'move0.gif' , path + 'move1.gif' , path + 'move2.gif'])
        self.add_state('jump' , delay, [path + 'jump0.gif' . path + 'jump1.gif' , path + 'jump2.gif'])
        self.add_state('idle', delay, [path + 'idle0.gif', path + 'idle1.gif', path + 'idle2.gif'])


class Game:
    """
    Sprite example declaration

    shelly = animations.Sprite()
    shelly.add_state('idle', 100, ['idle01.gif', 'idle02.gif', 'idle03.gif'])
    shelly.set_state('idle')
    """

    def __init__(self, stage, player_left_color, player_right_color):
        self.player_left = Player('left', player_left_color)        
        self.player_right = Player('right', player_right_color)
