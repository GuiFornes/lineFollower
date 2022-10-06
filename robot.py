import odometry
import utils
import threading
import pypot.dynamixel as dm
import time
import sys
import math

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
        self.move_speed = 1
        self.asked_speedL = 0
        self.asked_speedR = 0
        self.linear_speed = 0
        self.angular_speed = 0
        self.last_goal = [0, 0]

        # Init communication thread
        # self.com_thread = threading.Thread(target=self.__communicator)
        # self.com_thread.start()
        # self.time_thread = 0

    def get_location(self):
        return self.odom.position, self.odom.orientation

    def set_speed(self, speedL, speedR):
        self.asked_speedL = speedL * self.move_speed
        self.asked_speedR = speedR * self.move_speed

    def get_asked_speed(self):
        return self.asked_speedL, self.asked_speedR

    def get_real_speed(self):
        return self.odom.rot_speedL, self.odom.rot_speedR

    def follow_line(self, color=GREEN):
        print("[INFO] Following line ", color)
        while True:
            target = self.__compute_target(color)
            print("[INFO] Target: ", target)
            left, right = kinematics.go_to_xya(0, 0, 0, *target[0], target[1])
            print("[INFO] Left: ", left, "Right: ", right)
            self.set_speed(left, right)
            print("[INFO] Speed set: ", self.get_real_speed())
            self.__communicator()

    def __compute_target(self, color=GREEN):
        ret, goal = self.vision.update(color)  # in pixels
        if not ret:
            goal = self.odom.position + [0, 0.01], self.odom.orientation
        else:
            goal = self.odom.position + kinematics.pixel_to_robot(*goal), self.odom.orientation + math.atan2(goal[0],
                                                                                                             goal[1])
            self.last_goal = goal
        return goal  # meters, world frame

    def go_to_objective(self):
        pass

    def where_did_i_go(self):
        print("[INFO] Position: ", self.odom.position, self.odom.orientation)
        print("[INFO] Now compliant for 5 seconds: ", )
        self.compliant()
        t = time.time()
        while time.time()-t < 5:
            self.__communicator()
        self.non_compliant()
        print("[INFO] No more compliant")
        print("[INFO] Position: ", self.odom.position, self.odom.orientation)

        return self.odom.position, self.odom.orientation

    def draw_me_a_map(self):
        pass

    def non_compliant(self):
        self.dxl_io.set_torque_limit({2: 100, 5: 100})

    def compliant(self):
        self.dxl_io.set_torque_limit({2: 0, 5: 0})

    def __communicator(self):
        # print("[INFO] Communicator thread started")
        while True:
            t = time.time()
            # Enable motors
            """
            print("[INFO] reading keyboard entry")
            input_kb = str(sys.stdin.readline()).strip("\n")
            if input_kb == "s":
                self.compliant()
            if input_kb == "r":
                self.non_compliant()
            """
            # Send orders
            # print("[INFO] Sending orders")
            self.dxl_io.set_moving_speed({2: math.degrees(self.asked_speedL)})
            self.dxl_io.set_moving_speed({5: math.degrees(-self.asked_speedR)})

            # Update robot information
            # print("[INFO] Updating robot information")
            # print("[INFO] Reading encoders : ", self.dxl_io.get_present_speed((2, 5)))
            speedL, speedR = self.dxl_io.get_present_speed([2, 5])

            self.odom.rot_speedL = math.radians(speedL)
            self.odom.rot_speedR = math.radians(-speedR)
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
