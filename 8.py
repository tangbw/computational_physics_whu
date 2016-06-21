from pylab import *

g = 9.8
l = 1

class state:
    def __init__(self, _x, _vx, _t):
        self.x = _x
        self.vx = _vx
        self.t = _t
        
class pendulum:
    def __init__(self, _s = state( 0, 0, 0), _dt = 0):
        self.pendulum_state = []
        self.pendulum_state.append(_s)
        self.dt = _dt
        
    def next_state(self,current_state):
        global g,l 
        next_vx = current_state.vx - g * current_state.x * self.dt / l
        next_x = current_state.x + next_vx * self.dt
        return state( next_x, next_vx, current_state.t + self.dt)
        
    def move(self):
        while not (self.pendulum_state[-1].t > 1):
            self.pendulum_state.append(self.next_state(self.pendulum_state[-1]))
            
    def trajectory(self):
        x = []
        t = []
        for s in self.pendulum_state:
            x.append(s.x)
            t.append(s.t)
            
        plot(t,x)
        
a = pendulum(state( 0, 20, 0), _dt = 0.01)
a.move()
a.trajectory()
show()
