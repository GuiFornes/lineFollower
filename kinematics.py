from constants import *


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
    elif speedL == -speedR:
        return 0, speedL / L
    else:
        rot_center = L * (speedL + speedR) / (2 * (speedR - speedL))
        return (speedL + speedR) / 2, (speedR - speedL) / L


def odometry(linear, angular, t):
    """
    This function calculates the variation of position of the robot
    :param linear: linear velocity (m/s)
    :param angular: angular velocity (rad/s)
    :param t: time (s)
    :return: dx, dy, dtheta (m, m, rad)
    """
    pass


def tick_odom(x, y, theta, linear, angular, t):
    """
    This function calculates the new position of the robot in world frame
    :param x: current x position (m)
    :param y: current y position (m)
    :param theta: current theta (rad)
    :param linear: linear velocity (m/s)
    :param angular: angular velocity (rad/s)
    :param t: time (s)
    :return: dx, dy, dtheta (m, m, rad)
    """
    pass


def inverse_kinematics(linear, angular):
    """
    This function calculates the wheel speeds
    :param linear: linear velocity (m/s)
    :param angular: angular velocity (rad/s)
    :return: left wheel speed, right wheel speed (rad/s)
    """
    pass


def go_to_xya(x, y, theta):
    """
    This function calculates the wheel speeds to go to a specific position
    :param x: x position (m)
    :param y: y position (m)
    :param theta: theta (rad)
    :return: left wheel speed, right wheel speed (rad/s)
    """
    pass


def pixel_to_robot(x, y):
    """
    This function converts the pixel coordinates to robot coordinates
    :param x: x position (pixel)
    :param y: y position (pixel)
    :return: x, y, z (m)
    """
    pass


def pixel_to_world(x, y):
    """
    This function converts the pixel coordinates to world coordinates
    :param x: x position (pixel)
    :param y: y position (pixel)
    :return: x, y, z (m)
    """
    pass
