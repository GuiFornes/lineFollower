from robot import Robot

BLUE, RED, GREEN = 0, 1, 2

firstBot = Robot()

try:
    firstBot.follow_line(color=BLUE)
except KeyboardInterrupt:
    print("[INFO] Stopping robot, bye bye")
finally:
    firstBot.set_speed(0, 0)
    firstBot.disable_tork()  # Disable motors instead (disable tork)
