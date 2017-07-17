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
