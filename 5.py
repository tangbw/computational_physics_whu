import pylab as pl
import pickle

class Q1_4:
    """
        Show the answer of question 1_4
        initial na=1000 nb=0
    """
    def __init__(self, na = 1000,nb = 0.0, taua = 1.0,taub = 2.0, dt = 0.1, time = 3.0):
        self.taua = taua
        self.taub = taub
        self.dt = dt
        self.na = na
        self.nb = nb
        self.time = time

    def __str__(self):
        msg = "There are %d A at the beginning,there are %d B at the beginning,\
and the decay time constant is set to be %f 'a',%f 'b'"%(self.na, self.nb, self.taua, self.taub)
        return msg

    def calculate(self):
        self.n_A = []
        self.n_B = []
        self.T = []
        self.n_A.append(self.na)
        self.n_B.append(self.nb)
        self.T.append(0)
        nsteps = int(self.time / self.dt)
        for i in range(1, nsteps):
            self.n_A.append(self.n_A[i - 1] - self.n_A[i - 1] / self.taua * self.dt)
            self.n_B.append(self.n_B[i - 1]+self.n_A[i - 1]/self.taua*self.dt-self.n_B[i-1]/self.taub*self.dt)
            self.T.append(self.T[i - 1] + self.dt)
        return 0

    def plot(self):
        pl.plot(self.T, self.n_A, 'r-*' )
        pl.plot(self.T, self.n_B, 'b-*' )
        pl.title("A and B's Decay")
        pl.xlabel("time")
        pl.ylabel("Number of Nuclei")
        pl.show()
        pl.savefig("1_4.jpg")
    
    
A = Q1_4(1000, 0.0, 1.0, 2.0, 0.1, 3)
print A.__doc__
print A

A.calculate()
A.plot()
