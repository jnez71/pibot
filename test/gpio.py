#!/usr/bin/env python
from __future__ import division
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # broadcom pin numbering scheme
LED = 18
GPIO.setup(LED, GPIO.OUT)
SWITCH = 23
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press CTRL+C to exit...")
try:
    while True:
        time.sleep(0.1)
        if GPIO.input(SWITCH): continue
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
