import numpy as np

"""
This file contains all the constants used in the project.
"""
RADIUS = 0.025  # radius of the wheels (m)
L = 0.12  # Distance between the wheels (m)

ORIGIN = 320, 480  # Origin of the robot (pixels)
SCALE = 0.047/640, 0.036/480  # Scale of the camera (m/pixel) 0.042/640

BLUE, RED, GREEN = 0, 1, 2  # Green not programmed yet in vision part
COLOR_BOUND = [  # HSV
    (np.array([89, 122, 83]), np.array([142, 255, 241])),  # BLUE
    (np.array([0, 72, 0]), np.array([15, 255, 255])),  # RED
    (np.array([27, 36, 80]), np.array([86, 255, 238])),  # GREEN
]
