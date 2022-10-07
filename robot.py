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
        self.move_speed = 1.5  # rad/s
        self.asked_speedL = 0
        self.asked_speedR = 0
        self.linear_speed = 0
        self.angular_speed = 0
        self.last_goal = [0, 0]

        # Init PID
        self.previous_error = 0
        self.tmp_prev = time.time()
        self.kp = 0.15
        self.Kd = 0.01
        self.kpa = 1
        self.kpd = 300
        self.Kp_theta = 100

        # Init communication thread
        # self.com_thread = threading.Thread(target=self.communicator)
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

    def follower(self):
        self.non_compliant()
        color = GREEN
        for color in [GREEN, BLUE, RED]:
            self.follow_line(color)

    def follow_line(self, color=GREEN):
        print("[INFO] Following line ", color)
        t = time.time()
        while (not self.vision.detect_yellow()) or time.time() - t < 5:
            t = time.time()
            ret, goal = self.vision.update(color)
            if not ret:
                left, right = self.move_speed, self.move_speed
            else:
                left, right = self.__pid(*goal)
            self.set_speed(left, right)
            print("[INFO] Speed set: ", self.get_asked_speed())
            self.communicator()

    def __pid(self, x, y):
        error = x - 320  # middle of the img
        print("error : ", error)
        correction = self.kp * error + self.Kd * (error - self.previous_error) / (time.time() - self.tmp_prev)
        self.previous_error = error
        self.tmp_prev = time.time()
        left_instruction = self.move_speed + math.radians(correction)
        right_instruction = self.move_speed - math.radians(correction)
        if left_instruction > 2 * np.pi:
            right_instruction = right_instruction - (left_instruction - 2 * np.pi)
            left_instruction = 2 * np.pi
        elif left_instruction < -2 * np.pi:
            right_instruction = right_instruction + (-2 * np.pi - left_instruction)
            left_instruction = -2 * np.pi
        if right_instruction > 2 * np.pi:
            left_instruction = left_instruction - (right_instruction - 2 * np.pi)
            right_instruction = 2 * np.pi
        elif right_instruction < -2 * np.pi:
            left_instruction = left_instruction + (-2 * np.pi - right_instruction)
            right_instruction = -2 * np.pi
        return left_instruction, right_instruction

    def go_to_objective(self):
        pass

    def where_did_i_go(self):
        print("\n[INFO] Position: ", self.odom.position, self.odom.orientation)
        print("[INFO] Now compliant for infini seconds: ", )
        self.compliant()
        t = time.time()
        try:
            while True:
                self.communicator()
                # print("[INFO] Position: ", self.odom.position, self.odom.orientation)
        except KeyboardInterrupt:
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

    def communicator(self):
        # print("[INFO] communicator thread started")

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
        # print("[INFO] Sending orders", self.get_asked_speed())
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
