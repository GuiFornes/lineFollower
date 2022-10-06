#! /usr/bin/env python3
from robot import Robot
import time

BLUE, RED, GREEN = 0, 1, 2

print("[INFO] Connecting to motors ...")
firstBot = Robot()
print("[INFO] FirstBot is ready to go")

follow = False

if follow:
    try:
        firstBot.follow_line(color=GREEN)
    except KeyboardInterrupt:
        print("[INFO] Stopping robot, bye bye")
    finally:
        firstBot.set_speed(0, 0)
        firstBot.compliant()

else:
    firstBot.compliant()
    t_robot = time.time()
    try:
        while True:
            print("[INFO] motor speed: ", firstBot.get_real_speed())
            print("[INFO] position: ", firstBot.get_location())
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("time robot = ", time.time() - t_robot)
        print("time_thread = ", firstBot.time_thread)