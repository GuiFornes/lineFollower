import numpy as np
from math import sqrt
import matplotlib.pyplot as plt


def rotation_matrix(alpha):
    """Return a 2D rotation matrix."""
    return np.array([[np.cos(alpha), -np.sin(alpha)],
                     [np.sin(alpha), np.cos(alpha)]])


def circumscribed_circle(A, B, C):
    """
    Return the center and radius of the circumscribed circle of the triangle
    ABC.
    :param A: first point of the trajectory
    :param B: second point
    :param C: third point
    :return: center and radius of the circumscribed circle
    """
    a = np.linalg.norm(B - C)
    b = np.linalg.norm(C - A)
    c = np.linalg.norm(A - B)
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    rad = a * b * c / (4 * area)
    alpha = np.arccos((a**2 + c**2 - b**2) / (2 * a * c))
    beta = np.arccos((a**2 + b**2 - c**2) / (2 * a * b))
    gamma = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    cen = (A * np.sin(2 * np.pi - alpha) + B * np.sin(2 * np.pi - beta)
              + C * np.sin(2 * np.pi - gamma)) / (np.sin(2 * np.pi - alpha)
                                                  + np.sin(2 * np.pi - beta)
                                                  + np.sin(2 * np.pi - gamma))
    return cen, rad


def rad_to_deg_second(rad):
    """Convert radian/s to degree/s."""
    return rad * 180 / np.pi


def deg_to_rad_second(deg):
    """Convert degrees to radians."""
    return deg * np.pi / 180



if __name__ == "__main__":
    A = np.array([0, 0])
    B = np.array([1, 1])
    C = np.array([2, 4])
    center, radius = circumscribed_circle(A, B, C)
    plt.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]])
    plt.plot(center[0], center[1], 'o')
    plt.Circle((center[0], center[1]), radius)
    plt.show()

