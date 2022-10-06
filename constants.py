import numpy as np

"""
This file contains all the constants used in the project.
"""
RADIUS = 0.0245  # radius of the wheels (m)
L = 0.13  # Distance between the wheels (m)

ORIGIN = 320, 480  # Origin of the robot (pixels)
SCALE = 0.047/640, 0.036/480  # Scale of the camera (m/pixel) 0.042/640

GREEN, BLUE, RED, YELLOW = 0, 1, 2, 3  # Green not programmed yet in vision part
COLOR_BOUND = [  # HSV
    (np.array([57, 70, 79]), np.array([83, 255, 229])),  # GREEN
    (np.array([89, 122, 83]), np.array([142, 255, 241])),  # BLUE
    (np.array([0, 72, 0]), np.array([15, 255, 255]))  # RED
]
