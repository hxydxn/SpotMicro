import board
import digitalio
import busio
from adafruit_servokit import ServoKit
import adafruit_motor.servo

kit = ServoKit(channels=16)
kit.servo[0].angle = 0