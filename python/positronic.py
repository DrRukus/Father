#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

print "Beginning program..."

GPIO.setmode(GPIO.BCM) ## Use BCM numbering
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT) ## Setup GPIO Pin 4 to OUT

stopTime = time.time() + 30
while time.time() < stopTime:
    GPIO.output(4,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4,GPIO.LOW)
    time.sleep(1)
