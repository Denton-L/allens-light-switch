#!/usr/bin/env python2

import RPi.GPIO as GPIO

class Motor:
    PORT = 18
    PWM_PERIOD = 20.0

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PORT, GPIO.OUT)
        self.pwm = GPIO.PWM(self.PORT, 1.0 / 1000.0 * self.PWM_PERIOD)
        self.pwm.start(0.0)

    def __changeDutyCycle(self, milliseconds):
        print(milliseconds)
        self.pwm.ChangeDutyCycle(milliseconds / self.PWM_PERIOD * 100.0)

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()

    def up(self):
        self.__changeDutyCycle(1.0)

    def middle(self):
        self.__changeDutyCycle(1.5)


    def down(self):
        self.__changeDutyCycle(2.0)

if __name__ == '__main__':
    from time import sleep

    motor = Motor()
    try:
        while True:
            motor.up()
            sleep(0.5)
            motor.middle()
            sleep(0.5)
            motor.down()
            sleep(0.5)
            motor.middle()
            sleep(0.5)
    finally:
        motor.cleanup()
