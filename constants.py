import numpy as np

"""
This file contains all the constants used in the project.
"""
RADIUS = 0.025  # radius of the wheels (m)
L = 0.12  # Distance between the wheels (m)

ORIGIN = 320, 480  # Origin of the robot (pixels)
SCALE = 0.042/640, 0.039/480  # Scale of the camera (m/pixel) 0.042/640

BLUE, RED, GREEN = 0, 1, 2  # Green not programmed yet in vision part
COLOR_BOUND = [  # HSV
    (np.array([0, 40, 85]), np.array([80, 255, 255])),  # BLUE
    (np.array([45, 40, 0]), np.array([100, 255, 255])),  # RED
    (np.array([100, 75, 65]), np.array([120, 185, 255])),  # GREEN
]
