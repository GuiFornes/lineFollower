import numpy as np
import kinematics as kin
from constants import *


class Odometry:
    def __init__(self, x=0, y=0, theta=0):
        self.position = np.array([0, 0])
        self.orientation = 0
        self.rot_speedL = 0
        self.rot_speedR = 0
        self.lin_speedL = 0
        self.lin_speedR = 0

    def update(self, t):
        linear, angular = kin.direct_kinematics(self.rot_speedL, self.rot_speedR)
        self.position, self.orientation = \
            kin.tick_odom(self.position[0], self.position[1], self.orientation, linear, angular, t)

    def compute_linear_speed(self):
        self.lin_speedL = self.rot_speedL * RADIUS
        self.lin_speedR = self.rot_speedR * RADIUS
