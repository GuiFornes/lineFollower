#! /usr/bin/env python3
from robot import Robot
from constants import *
import time
import kinematics as kin

GREEN, BLUE, RED, YELLOW = 0, 1, 2, 3

print("[INFO] Connecting to motors ...")
firstBot = Robot()
print("[INFO] FirstBot is ready to go")

try:
    firstBot.non_compliant()
    speed,timing = kin.go_to_xya(0.2,0.2,2.5*RADIUS)
    print(f"speedL:{speed[0]} , speedR:{speed[1]}")
    firstBot.set_speed(speed[0], speed[1])
    print(firstBot.get_asked_speed())
    firstBot.communicator()
    time.sleep(timing)
except KeyboardInterrupt:
    print("[INFO] Stopping robot, bye bye")
finally:
    firstBot.set_speed(0, 0)
    firstBot.compliant()


