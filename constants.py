import numpy as np

"""
This file contains all the constants used in the project.
"""
RADIUS = 0.0245  # radius of the wheels (m)
L = 0.132  # Distance between the wheels (m)

ORIGIN = 320, 480  # Origin of the robot (pixels)
SCALE = 0.047/640, 0.036/480  # Scale of the camera (m/pixel) 0.042/640

GREEN, BLUE, RED, YELLOW = 0, 1, 2, 3  # Green not programmed yet in vision part
COLOR_BOUND = [  # HSV
    (np.array([73, 137, 119]), np.array([79, 255, 228])),  # GREEN
    (np.array([99, 90, 145]), np.array([102, 255, 255])),  # BLUE
    (np.array([0, 160, 161]), np.array([10, 254, 255]))  # RED
]
