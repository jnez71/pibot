#!/usr/bin/env python
from __future__ import division
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import cv2

camera = PiCamera()
capture_buff = PiRGBArray(camera)
time.sleep(0.1)

camera.capture(capture_buff, format="bgr")
img = capture_buff.array  # numpy array

cv2.imshow("Image", img)
print("Press any key to quit...")
cv2.waitKey(0)
