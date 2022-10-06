from robot import Robot
import time

BLUE, RED, GREEN = 0, 1, 2

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
    while True:
        print("[INFO] motor speed: ", firstBot.get_real_speed())
        print("[INFO] position: ", firstBot.get_location())
        time.sleep(0.5)
