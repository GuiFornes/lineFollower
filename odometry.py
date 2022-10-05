import numpy as np


class Odometry:
    def __init__(self, x=0, y=0, theta=0):
        self.position = np.array([0, 0])
        self.orientation = 0
        self.posL = 0
        self.posR = 0
        self.real_speedL = 0
        self.real_speedR = 0

    def update(self, posL, posR, t):
        pass
    