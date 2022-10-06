#! /usr/bin/env python3
from robot import Robot
import time
import kinematics as kin

GREEN, BLUE, RED, YELLOW = 0, 1, 2, 3

print("[INFO] Connecting to motors ...")
firstBot = Robot()
print("[INFO] FirstBot is ready to go")

try:
    firstBot.kin.go_to_xya(*firstBot.odom.position, firstBot.odom.orientation, 0.1, 0 , 0)
except KeyboardInterrupt:
    print("[INFO] Stopping robot, bye bye")
finally:
    firstBot.set_speed(0, 0)
    firstBot.compliant()


