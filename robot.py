import odometry
import utils
import threading
import pypot.dynamixel as dm
import time
import sys

from constants import *
import kinematics
import vision
import odometry


class Robot:
    def __init__(self):
        # Init motors
        ports = dm.get_available_ports()
        if not ports:
            exit('No port')
        self.dxl_io = dm.DxlIO(ports[0])
        # motor_ids = self.dxl_io(ports[0]).scan()
        self.dxl_io.set_wheel_mode([2])
        self.dxl_io.set_wheel_mode([5])

        # Init vision and camera
        self.vision = vision.Vision()

        # Init odometry
        self.odom = odometry.Odometry()

        # Init variables
        self.asked_speedL = 0
        self.asked_speedR = 0
        self.linear_speed = 0
        self.angular_speed = 0
        self.last_goal = [0, 0]

        # Init communication thread
        self.com_thread = threading.Thread(target=self.__communicator)
        self.com_thread.start()

    def get_location(self):
        return self.odom.position, self.odom.orientation

    def set_speed(self, speedL, speedR):
        self.speedL = speedL
        self.speedR = speedR

    def get_speed(self):
        return self.speedL, self.speedR

    def follow_line(self, color=GREEN):
        print("[INFO] Following line ", color)
        while True:
            target = self.__compute_target(color)
            left, right = kinematics.go_to_xya(0, 0, 0, *target[0], target[1])
            self.set_speed(left, right)

    def __compute_target(self, color=GREEN):
        ret, goal = self.vision.update(color)  # in pixels
        if ret:
            goal = self.odom.position + [0, 0.005], self.odom.orientation
        else:
            goal = self.odom.position + kinematics.pixel_to_robot(*goal), self.odom.orientation + np.atan2(goal[0], goal[1])
            self.last_goal = goal
        return goal  # meters, world frame

    def go_to_objective(self):
        pass

    def where_did_i_go(self):
        print("[INFO] Position: ", self.odom.position, self.odom.orientation)
        print("[INFO] Now compliant for 5 seconds: ", )
        self.compliant()
        time.sleep(5)
        self.non_compliant()
        print("[INFO] Non-compliant again")
        print("[INFO] Position: ", self.odom.position, self.odom.orientation)

        return self.odom.position, self.odom.orientation

    def draw_me_a_map(self):
        pass

    def non_compliant(self):
        self.dxl_io.enable_torque([2, 5])

    def compliant(self):
        self.dxl_io.disable_torque([2, 5])

    def __communicator(self):
        while True:
            t = time.time()
            # Enable motors
            input_kb = str(sys.stdin.readline()).strip("\n")
            if input_kb == "s":
                self.compliant()
            if input_kb == "r":
                self.non_compliant()

            # Send orders
            self.dxl_io.set_moving_speed({2: utils.rad_to_deg_second(self.speedL)})
            self.dxl_io.set_moving_speed({5: utils.rad_to_deg_second(-self.speedR)})

            # Update robot information
            self.odom.real_speedL = utils.deg_to_rad_second(self.dxl_io.get_present_speed((2,)))
            self.odom.real_speedR = utils.deg_to_rad_second(-self.dxl_io.get_present_speed((5,)))
            self.odom.update(time.time() - t)
            time.sleep(0.1)


if __name__ == "__main__":
    firstBot = Robot()

    firstBot.set_speed(100, -100)
    time.sleep(2)
    firstBot.set_speed(0, 0)
    print("[INFO] Now compliant for 5 seconds")
    firstBot.compliant()
    time.sleep(5)
    print("[INFO] Now non compliant")
    print("[INFO] firstBot in : ", firstBot.get_location())
