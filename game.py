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
        path = color + '/' + ('left/' if direction is 'left' else 'right/')
        self.add_state('duck_down', delay, [path + 'duck_down_00.gif', path + 'duck_down_01.gif', path + 'duck_down_02.gif'])
        self.add_state('duck_up', delay, [path + 'duck_up_00.gif', path + 'duck_up_01.gif', path + 'duck_up_02.gif'])                               
        self.add_state('punch' , delay, [path + 'punch_00.gif' , path + 'punch_01.gif' , path + 'punch_02.gif'])
        self.add_state('move' , delay, [path + 'move_00.gif' , path + 'move_01.gif' , path + 'move_02.gif'])
        self.add_state('jump' , delay, [path + 'jump_00.gif' . path + 'jump_01.gif' , path + 'jump_02.gif'])
        self.add_state('idle', delay, [path + 'idle_00.gif', path + 'idle_01.gif', path + 'idle_02.gif'])


class Game:
    """
    Sprite example declaration

    shelly = animations.Sprite()
    shelly.add_state('idle', 100, ['idle01.gif', 'idle02.gif', 'idle03.gif'])
    shelly.set_state('idle')
    """

    def __init__(self, player_left_color, player_right_color):
        self.player_left = Player('left', player_left_color)        
        self.player_right = Player('right', player_right_color)


