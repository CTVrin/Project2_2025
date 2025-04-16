import RPi.GPIO as GPIO
import time

#Name: Zhang you
#Date: 2025/4/16

# GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Water Detected!")
    else:
        print("Water Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # detect the pin goes high or low 
GPIO.add_event_callback(channel, callback)  # set call back function

while True:
    time.sleep(1)
