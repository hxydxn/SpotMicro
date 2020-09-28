# import board
# import digitalio
# import busio
# from adafruit_servokit import ServoKit
# import adafruit_motor.servo

# i2c_bus = busio.I2C(board.SCL, board.SDA);
# i2c_bus2 = busio.I2C(board.SCL_1, board.SDA_1);
# kit = ServoKit(channels=16, i2c=i2c_bus)
# kit2 = ServoKit(channels=16, i2c=i2c_bus2)

class SpotMicroDriver:

    def test(self):
        print("test")
    # def __init__(self, bus_count):
    #     self.kit = ServoKit(channels=16, i2c=busio.I2C(board.SCL, board.SDA))
    #     self.kit2 = ServoKit(channels=16, i2c=busio.I2C(board.SCL_1, board.SDA_1))
    #     super().__init__()

    # def set_servo_angle(self, board_id, port, angle):
    #     if (board_id == 1):
    #         self.kit.servo[port].angle = angle
    #     else:
    #         self.kit2.servo[port].angle = angle
