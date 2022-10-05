import utils
import vision
import numpy as np

RED, BLUE, GREEN = 0, 1, 2  # Green not programmed yet in vision part


class Robot:
    def __init__(self):
        self.vision = vision.Vision()
        self.position = np.array([0, 0])
        self.orientation = 0
        self.speedL = 0
        self.speedR = 0

    def order_motors(self):
        pass

    def get_position(self):
        return self.position

    def follow_line(self, color=RED):
        self.compute_traj(color)

    def compute_target(self, color=RED):
        ret, objectives = self.vision.update(color)
        if not ret:
            exit(0)  # WARNING: line not found
        center, radius = utils.circumscribed_circle(objectives[0], objectives[1], objectives[2])


    def update_position(self):  # Odometry, divide in thread ?
        pass

    def go_to_objective(self):
        pass

    def where_did_i_go(self):
        pass

    def draw_me_a_map(self):
        pass


