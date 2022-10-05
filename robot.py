import utils
import vision
import threading
import pypot.dynamixel as dm
import time
import sys

from constants import *
import kinematics


class Robot:
    def __init__(self):
        # Init motors
        ports = dm.get_available_ports()
        if not ports:
            exit('No port')
        self.dxl_io = dm.DxlIO(ports[0])
        motor_ids = self.dxl_io(ports[0]).scan()
        self.dxl_io.set_wheel_mode(motor_ids[0])
        self.dxl_io.set_wheel_mode(motor_ids[1])

        # Init vision and camera
        self.vision = vision.Vision()

        # Init variables
        self.position = np.array([0, 0])
        self.orientation = 0
        self.speedL = 0
        self.speedR = 0
        self.posL = 0
        self.posR = 0
        self.linear_speed = 0
        self.angular_speed = 0
        self.traj_buffer = [0, 0]

        # Init communication thread
        self.com_thread = threading.Thread(target=self.__communicator)
        self.com_thread.start()

    def get_position(self):
        return self.position

    def set_speed(self, speedL, speedR):
        self.speedL = speedL
        self.speedR = speedR

    def get_speed(self):
        return self.speedL, self.speedR

    def follow_line(self, color=RED):
        target = self.__compute_target(color)
        left, right = kinematics.go_to_xya(0, 0, 0, target[0], target[1], 0)
        self.set_speed(left, right)

    def __compute_target(self, color=RED):
        ret, objectives = self.vision.update(color)
        if ret:
            goal = 0, 0.005, 0
        else:
            pt = objectives[0]
            goal = pt[0], pt[1], np.atan2(pt[0], pt[1])
        return goal

    def update_position(self):
        pass

    def go_to_objective(self):
        pass

    def where_did_i_go(self):
        pass

    def draw_me_a_map(self):
        pass

    def enable_tork(self):
        self.dxl_io.enable_torque([2, 5])

    def disable_tork(self):
        self.dxl_io.disable_torque([2, 5])

    def __communicator(self):
        while True:
            # Enable motors
            input_kb = str(sys.stdin.readline()).strip("\n")
            if input_kb == "s":
                self.disable_tork()
            if input_kb == "r":
                self.enable_tork()

            # Send orders
            self.dxl_io.set_moving_speed({2: utils.rad_to_deg_second(-self.speedL)})
            self.dxl_io.set_moving_speed({5: utils.rad_to_deg_second(self.speedR)})

            # Update robot information
            self.posL = utils.deg_to_rad(self.dxl_io.get_present_position((2,)))
            self.posR = utils.deg_to_rad(self.dxl_io.get_present_position((5,)))
            time.sleep(0.1)
