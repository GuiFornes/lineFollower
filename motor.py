import pypot.dynamixel as dm

ports = dm.get_available_ports()

print(ports)
if not ports:
    exit('No port')

dxl_io = dm.DxlIO(ports[0])
dxl_io.set_wheel_mode([1])
dxl_io.set_moving_speed({1: 360}) # Degrees / s