import RPi.GPIO as GPIO


class ServoService:

    def __init__(self):
        self.servo_pin = None
        self.servo_pin_nr = 12

    def __setup_module(self):
        GPIO.setmode(GPIO.BOARD)
        self.servo_pin = GPIO.PWM(self.servo_pin_nr, 50)
        GPIO.setup(self.servo_pin_nr, GPIO.OUT)

        self.servo_pin.start(7.5)

    def move(self, dc):
        try:
            self.servo_pin.ChangeDutyCycle(dc)

        except KeyboardInterrupt:
            self.servo_pin.stop()
