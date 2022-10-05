import vision
import numpy as np

RED, BLUE, GREEN = 0, 1, 2  # Green not programmed yet in vision part


class Robot:
    def __init__(self):
        self.vision = vision.Vision()
        self.position = np.array([0, 0])

    def get_position(self):
        return self.position

    def follow_line(self, color=RED):
        pass

    def go_to_objective(self):
        pass

    def where_did_i_go(self):
        pass

    def draw_me_a_map(self):
        pass


