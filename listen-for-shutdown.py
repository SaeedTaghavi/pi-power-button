#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
from time import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    GPIO.wait_for_edge(3, GPIO.FALLING)
    t1 = time()
    while(GPIO.input(3)==0):
            t2=time()
            if (t2-t1>2):
                    subprocess.call(['shutdown', '-h', 'now'], shell=False)