#! /usr/bin/env python3
from robot import Robot
import time
form constants import *

print("[INFO] Connecting to motors ...")
firstBot = Robot()
print("[INFO] FirstBot is ready to go")

follow = True

if follow:
    try:
        firstBot.follow_line(color=GREEN)
    except KeyboardInterrupt:
        print("[INFO] Stopping robot, bye bye")
    finally:
        firstBot.set_speed(0, 0)
        firstBot.compliant()

else:
    try:
        firstBot.where_did_i_go()
    except KeyboardInterrupt:
        print("[INFO] Position & Angle: ", firstBot.odom.position, firstBot.odom.orientation)
