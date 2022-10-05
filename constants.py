import numpy as np

"""
This file contains all the constants used in the project.
"""
RADIUS = 0  # radius of the wheels (m)
L = 10  # Distance between the wheels (m)

ORIGIN = 320, 480  # Origin of the robot (pixels)
SCALE = 0.042/640, 0.039/480  # Scale of the camera (m/pixel) 0.042/640

BLUE, RED, GREEN = 0, 1, 2  # Green not programmed yet in vision part
COLOR_BOUND = [  # BGR
    (np.array([175, 75, 0]), np.array([255, 200, 130])),  # BLUE
    (np.array([60, 50, 180]), np.array([200, 150, 255])),  # RED
]
