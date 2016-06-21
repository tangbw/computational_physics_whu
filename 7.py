from pylab import *

g = 9.8
b2m = 1e-5
S0m = 1e-4
w = 2000

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class bassball:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.bassball_flight_state = []
        self.bassball_flight_state.append(_fs)
        self.dt = _dt
        print self.bassball_flight_state[-1].x, self.bassball_flight_state[-1].y, self.bassball_flight_state[-1].vx, self.bassball_flight_state[-1].vy

    def next_state(self, current_state):
        global g, b2m, S0m, w
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt - S0m * w * current_state.vy * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy + S0m * w * current_state.vx * self.dt - g * self.dt - b2m * v * current_state.vy * self.dt
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

    def shoot(self):
        while not(self.bassball_flight_state[-1].y < 0):
            self.bassball_flight_state.append(self.next_state(self.bassball_flight_state[-1]))
            print self.bassball_flight_state[-1].x, self.bassball_flight_state[-1].y, self.bassball_flight_state[-1].vx, self.bassball_flight_state[-1].vy

        r = - self.bassball_flight_state[-2].y / self.bassball_flight_state[-1].y
        self.bassball_flight_state[-1].x = (self.bassball_flight_state[-2].x + r * self.bassball_flight_state[-1].x) / (r + 1)
        self.bassball_flight_state[-1].y = 0

    def show_trajectory(self):
        x = []
        y = []
        for fs in self.bassball_flight_state:
            x.append(fs.x)
            y.append(fs.y)

        plot(x,y)

a = bassball(flight_state(0, 0, 50, 50, 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
show()
