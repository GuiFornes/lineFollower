import numpy as np


def rotation_matrix(alpha):
    """Return a 2D rotation matrix."""
    return np.array([[np.cos(alpha), -np.sin(alpha)],
                     [np.sin(alpha), np.cos(alpha)]])
