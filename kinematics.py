from constants import *
import utils
import numpy as np


def direct_kinematics(rotSpeedL, rotSpeedR):
    """
    This function calculates the linear (m/s) and angular (rad/s) velocity of the robot
    :param rotSpeedL: left wheel speed (rad/s)
    :param rotSpeedR: right wheel speed (rad/s)
    :return: linear, angular velocity (m/s, rad/s)
    """
    speedL, speedR = rotSpeedL * RADIUS, rotSpeedR * RADIUS
    if speedL == speedR:
        return speedL, 0
    else:
        return (speedL + speedR) / 2, 20 * (speedR - speedL) / L


def odom(linear, angular, t):
    """
    This function calculates the variation of position of the robot
    :param linear: linear velocity (m/s)
    :param angular: angular velocity (rad/s)
    :param t: time (s)
    :return: dx, dy, dtheta (m, m, rad)
    """
    # print(f"lin, ang : {linear:.5f}, {angular:.5f}")
    if angular == 0:
        dx, dy, dtheta = 0, linear * t, 0
    else:
        dx = (linear / angular) * (1 - np.cos(angular * t))
        dy = (linear / angular) * np.sin(angular * t)
        dtheta = angular * t
    # print(f"vitesse : {(dy/t)*100:.1f}")
    return dx*20, dy*20, dtheta


def tick_odom(x, y, theta, linear, angular, t):
    """
    This function calculates the new position of the robot in world frame
    :param x: current x position (m)
    :param y: current y position (m)
    :param theta: current theta (rad)
    :param linear: linear velocity (m/s)
    :param angular: angular velocity (rad/s)
    :param t: time (s)
    :return: new_x, new_y, new_theta (m, m, rad)
    """
    dx, dy, dtheta = odom(linear, angular, t)
    return x + dy * np.sin(theta) + dx * np.cos(theta), y + dy * np.cos(theta) - dx * np.sin(theta), theta + dtheta


def inverse_kinematics(linear, angular):
    """
    This function calculates the wheel speeds
    :param linear: linear velocity (m/s)
    :param angular: angular velocity (rad/s)
    :return: left wheel speed, right wheel speed (rad/s)
    """
    speedL = 1 / RADIUS * (linear - angular * L/2)
    speedR = 1 / RADIUS * (linear + angular * L/2)
    return speedL, speedR


def go_to_xya(x, y,speed):
    """
    This function calculates the wheel speeds to go to a specific position in the world frame
    :param x: x position (m)
    :param y: y position (m)
    :param theta: theta (rad)
    :return: left wheel speed, right wheel speed (rad/s) and the time
    """

    distance = np.sqrt(x ** 2 + y ** 2)
    timing = distance/speed
    theta=np.arctan2(x,y)
    return (inverse_kinematics(speed,theta/timing),timing/2)


def pixel_to_robot(x, y):
    """
    This function converts the pixel coordinates to robot frame coordinates
    :param x: x position (pixel)
    :param y: y position (pixel)
    :return: x, y (m)
    """
    dx, dy = x - ORIGIN[0], y - ORIGIN[1]
    return dx * SCALE[0], dy * SCALE[1]


def pixel_to_world(x, y):
    """
    This function converts the pixel coordinates to world coordinates
    :param x: x position (pixel)
    :param y: y position (pixel)
    :return: x, y, z (m)
    """
    pass
