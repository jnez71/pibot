#!/usr/bin/env python
from __future__ import division
import time
import numpy as np
from Adafruit_BNO055 import BNO055

imu = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
if not imu.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

status, self_test, error = imu.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

print('Reading BNO055 data, press Ctrl-C to quit...')
while True:
    celsius = imu.read_temp()
    mag = imu.read_magnetometer()  # uT
    gyro = imu.read_gyroscope()  # deg/s
    acc = imu.read_accelerometer()  # m/s^2
    print "Accel: ", np.round(acc, 0), "Gyro: ", np.round(gyro, 0)
    time.sleep(0.05)
