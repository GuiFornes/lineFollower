import cv2
import numpy as np

BLUE, RED = 0, 1

COLOR_BOUND = [  # BGR
    (np.array([175, 75, 0]), np.array([255, 200, 130])),  # BLUE
    (np.array([60, 50, 180]), np.array([200, 150, 255])),  # RED
]


class Vision:
    def __init__(self):
        self.cam = cv2.VideoCapture(2)
        self.frame = cv2.imread("frame.png")  # For testing
        self.filtered_frame = None
        self.range = [400, 300, 200]
        self.objectives = np.array([[0, 0], [0, 0], [0, 0]])

    def update(self, color=BLUE):
        self.__filter(color)
        return self.__get_objectives()

    def __filter(self, color=BLUE):
        ret, self.frame = self.cam.read()
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 0)
        mask = cv2.inRange(self.frame, COLOR_BOUND[color][0], COLOR_BOUND[color][1])
        mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        self.filtered_frame = self.frame & mask_rgb

    def __get_objectives(self):
        # 400, 300, 200
        # cv2.imshow("filtered", self.filtered_frame)
        # cv2.waitKey(0)
        self.range = [400, 300, 200]
        for obj in range(3):
            y = self.range[obj-1]
            pt1, pt2 = None, None
            for x in range(0, 640):
                if not np.array_equal(self.filtered_frame[y][x], np.array([0, 0, 0])):
                    pt1 = (x, y)
                    break
            for x in range(639, -1):
                if not np.array_equal(self.filtered_frame[y][x], np.array([0, 0, 0])):
                    pt2 = (x, y)
                    break
            if pt1 is None or pt2 is None:
                print("[INFO] No objectives found, trying another distance")
                if self.range[obj] < 25:
                    print("[WARN] No objectives found")
                    return False, None
                self.range[obj] -= 25
                obj -= 1
                continue
            self.objectives[obj] = np.mean(pt1 + pt2)
        return True, self.objectives

    def live_cam(self):
        _, frame = self.cam.read()
        cv2.imshow("frame", frame)

    def disp_image(self):
        cv2.imshow("image", self.frame)
        cv2.imshow("filtered", self.filtered_frame)


if __name__ == "__main__":
    vision = Vision()
    while True:
        vision.update()
        vision.disp_image()
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()
