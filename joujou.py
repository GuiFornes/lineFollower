import pypot.dynamixel as dm
import pybullet as p
import time

import os
os.environ['DISPLAY'] = ':0'

ports = dm.get_available_ports()
if not ports:
    exit('No port')
dxl_io = dm.DxlIO(ports[0])
# motor_ids = dxl_io(ports[0]).scan()
dxl_io.set_wheel_mode([2])
dxl_io.set_wheel_mode([5])


while True:
    keys = p.getKeyboardEvents()
    speedL, speedR = 0, 0
    if 122 in keys:
        speedL += 360
        speedR += -360
    if 115 in keys:
        speedL += 360
        speedR += -360
    if 113 in keys:
        speedL += 0
        speedR += -100
    if 100 in keys:
        speedL += 100
        speedR += 0

    dxl_io.set_moving_speed({2: speedL})
    dxl_io.set_moving_speed({5: speedR})
    time.sleep(0.1)
