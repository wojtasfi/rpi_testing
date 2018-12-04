import RPi.GPIO as GPIO


class ServoService:

    def __init__(self):
        self.servo_pin = None
        self.servo_pin_nr = 12
        self.initial_position = 6
        self.__setup_module()

    def __setup_module(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin_nr, GPIO.OUT)
        self.servo_pin = GPIO.PWM(self.servo_pin_nr, 50)

        self.servo_pin.start(self.initial_position)

    def move(self, dc):
        try:
            self.servo_pin.ChangeDutyCycle(float(dc))

        except KeyboardInterrupt:
            self.servo_pin.stop()
