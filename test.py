import pypot.dynamixel as dm
import time

ports = dm.get_available_ports()


if not ports:
    exit('No port')
dxl_io = dm.DxlIO(ports[0])
#motor_ids=dxl_io(ports[0]).scan()
dxl_io.set_wheel_mode([5])
dxl_io.set_moving_speed({2: 1000}) 
dxl_io.set_moving_speed({5: 1000})
time.sleep(3)

dxl_io.set_moving_speed({2: 0}) 
dxl_io.set_moving_speed({5: 0})