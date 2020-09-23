import board
import digitalio
import busio
from adafruit_servokit import ServoKit
import adafruit_motor.servo
import json

i2c_bus = busio.I2C(board.SCL, board.SDA);
i2c_bus2 = busio.I2C(board.SCL_1, board.SDA_1);
kit = ServoKit(channels=16, i2c=i2c_bus)
kit2 = ServoKit(channels=16, i2c=i2c_bus2)

with open('calibration.json') as infile:
    calib = json.load(infile)
    for board in calib:
        for leg in calib[board]:
            for pair in leg.items():
                if (int(board) == 0):
                    kit.servo[int(pair[0])].angle = int(pair[1])
                else:
                    kit.servo[int(pair[0])].angle = int(pair[1])