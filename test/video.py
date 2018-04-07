#!/usr/bin/env python
from __future__ import division
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import numpy as np
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 60
capture_buff = PiRGBArray(camera, size=camera.resolution)
time.sleep(0.1)

def find_centroid(channel):
    M = cv2.moments(channel)
    if(M["m00"]) > 1e-10:
        return tuple(map(int, (M["m10"]/M["m00"], M["m01"]/M["m00"])))
    return None

print("Press 'q' to quit...")
for frame in camera.capture_continuous(capture_buff, format="bgr", use_video_port=True):
    img = cv2.flip(frame.array, 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    reds = cv2.inRange(hsv, (160, 100, 50), (190, 255, 255))
    centroid = find_centroid(reds)
    if centroid: cv2.circle(img, centroid, 3, (255, 255, 255), thickness=10)
    cv2.imshow("Image and Red Centroid", img)
    key = cv2.waitKey(1)
    capture_buff.truncate(0)  # clear capture buffer (which is only size of camera.resolution)
    if key == ord("q"):
        break
