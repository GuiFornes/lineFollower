import gc
import pypot.dynamixel as dm
import keyboard
import time


ports = dm.get_available_ports()
if not ports:
    exit('No port')
dxl_io = dm.DxlIO(ports[0])
# motor_ids = dxl_io(ports[0]).scan()
dxl_io.set_wheel_mode([2])
dxl_io.set_wheel_mode([5])

print("ca marche")

while True:
    speedL, speedR = 0, 0
    if keyboard.is_pressed('z'):
        speedL += 360
        speedR += -360
    if keyboard.is_pressed('s'):
        speedL += 360
        speedR += -360
    if keyboard.is_pressed('q'):
        speedL += 0
        speedR += -100
    if keyboard.is_pressed('d'):
        speedL += 100
        speedR += 0

    dxl_io.set_moving_speed({2: speedL})
    dxl_io.set_moving_speed({5: speedR})
    time.sleep(0.1)
