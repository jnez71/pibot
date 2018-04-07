#!/usr/bin/env python
from __future__ import division
import RPi.GPIO as GPIO
import math
import time

GPIO.setmode(GPIO.BCM)  # broadcom pin numbering scheme
LED = 18
GPIO.setup(LED, GPIO.OUT)
pwm = GPIO.PWM(LED, 50)

period = 2  # s
start_time = time.time()
pwm.start(0)

print("Press CTRL+C to exit...")
try:
    while True:
        dc = abs(100*math.sin(2*math.pi*(time.time()-start_time)/period))
        pwm.ChangeDutyCycle(dc)
        # print(dc)
        time.sleep(0.01)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
