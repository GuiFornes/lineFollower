from robot import Robot

BLUE, RED, GREEN = 0, 1, 2

firstBot = Robot()
print("[INFO] FirstBot is ready to go")
try:
    firstBot.follow_line(color=GREEN)
except KeyboardInterrupt:
    print("[INFO] Stopping robot, bye bye")
finally:
    firstBot.set_speed(0, 0)
    firstBot.compliant()  # Disable motors instead (disable tork)
