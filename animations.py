import turtle
from threading import Timer

sprites = []

class State:
    def __init__(self, delay, shapes, repeats=True):
        self.delay = delay
        self.shapes = shapes
        self.index = 0
        self.repeats = repeats
        self.current_shape = self.shapes[self.index]
    
    def next(self):
        if self.index == len(self.shapes) - 1:
            if self.repeats:
                self.index = 0
            else:
                self.is_done = True
        else:
            self.index += 1
        self.current_shape = self.shapes[self.index]

    def start(self):
        self.index = 0
        self.current_shape = self.shapes[self.index]
        self.is_done = False
        self.run()
  
    def run(self):
        def func_wrapper():
            self.run()
            if not self.is_done:
                self.next()
        self.timer = Timer(self.delay, func_wrapper)
        self.timer.start()
  
    def stop(self):
        if self.timer:
            self.is_done = True
            self.timer.cancel()

class Sprite(turtle.Turtle):
    def __init__(self, states={}):
        super(Sprite, self).__init__()

        sprites.append(self)
    
        self.states = {}
        for key,state in states.items():
            self.states[key] = State(state["delay"] / 1000.0, state["shapes"], state["repeats"])
      
        self.current_state = None
    
    def add_state(self, name, delay, shapes, repeats=True):
        self.states[name] = State(delay / 1000.0, shapes, repeats)
    
    def set_state(self, name):
        assert name in self.states.keys()
        if self.current_state != self.states[name]:
            if self.current_state:
                self.current_state.stop()
                self.current_state.index = 0
            self.current_state = self.states[name]
            self.current_state.start()
    
    def update(self):
        self.shape(self.current_state.current_shape)

def update():
    for sprite in sprites:
        sprite.update()

if __name__ == "__main__":
    import os

    screen = turtle.Screen()
    screen.tracer(0)

    sprites_dir = os.getcwd() + '/sprites'
    os.chdir(sprites_dir + '/left')
    screen.addshape('duck_down_l.gif')
    screen.addshape('duck_up_l.gif')
    screen.addshape('idle_l.gif')
    screen.addshape('jump_l.gif')
    screen.addshape('move_right_l.gif')
    screen.addshape('punch_l.gif')

    shelly = Sprite()
    shelly.add_state('idle', 100, ['duck_down_l.gif', 'duck_up_l.gif', 'idle_l.gif'])
    shelly.add_state('attack', 100, ['duck_down_l.gif', 'duck_up_l.gif', 'idle_l.gif'])
    shelly.set_state('idle')

    while True:
        update()
        screen.update()