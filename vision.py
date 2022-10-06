import cv2
import numpy as np
import kinematics
from constants import *


class Vision:
    def __init__(self):
        try:
            self.cam = cv2.VideoCapture(2)
        except Exception as e:
            print("[ERROR] Camera not found")
            print(e)
            exit(1)
        self.frame = None  # cv2.imread("frame.png")  # For testing
        self.filtered_frame = None
        self.goal = np.array([0, 0])

    def update(self, color=GREEN):
        self.__filter(color)
        return self.__get_objectives()  # in pixels

    def __filter(self, color=GREEN):
        ret, self.frame = self.cam.read()
        hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)
        # equalize histogram
        hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
        hsv = cv2.GaussianBlur(hsv, (9, 9), 0)
        mask = cv2.inRange(hsv, COLOR_BOUND[color][0], COLOR_BOUND[color][1])
        self.filtered_frame = mask

    def __get_objectives(self):
        goal = np.array([0, 0])
        contours, _ = cv2.findContours(self.filtered_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 0:
            return False, goal
        contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        if cv2.contourArea(contour) < 1000:
            return False, goal
        moment = cv2.moments(contour)
        if moment["m00"] != 0:
            y = int(moment["m10"] / moment["m00"])
            x = int(moment["m01"] / moment["m00"])
            goal = np.array([x, y])
        return True, goal

    def detect_yellow(self):
        frame = self.frame
        contours, _ = cv2.findContours(self.filtered_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 0:
            return False
        contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        if cv2.contourArea(contour) < 1000:
            return False
        return True

    def live_cam(self):
        _, frame = self.cam.read()
        cv2.imshow("frame", frame)

    def disp_image(self):
        cv2.imshow("image", self.frame)
        mask = cv2.cvtColor(self.filtered_frame, cv2.COLOR_GRAY2BGR)
        filtered = self.frame & mask
        contours, _ = cv2.findContours(self.filtered_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) == 0:
            print("[INFO] No contour found")
            return
        contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        moment = cv2.moments(contour)
        print("Contour area = ", cv2.contourArea(contour))
        if cv2.contourArea(contour) < 10000:
            return
        if moment["m00"] != 0:
            x = int(moment["m10"] / moment["m00"])
            y = int(moment["m01"] / moment["m00"])
            cv2.circle(filtered, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("filtered", filtered)
            print("[INFO] Goal found at ({}, {})".format(x, y))


if __name__ == "__main__":
    vision = Vision()
    while True:
        vision.update(color=GREEN)
        vision.disp_image()
        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
    cv2.destroyAllWindows()