import RPi.GPIO as GPIO


class FlapsService:

    def __init__(self):
        self.right_servo_pin = None
        self.right_servo_pin_nr = 12
        self.left_servo_pin = None
        self.left_servo_pin_nr = 11
        self.initial_position = 6
        self.__setup_module()

    def __setup_module(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.right_servo_pin_nr, GPIO.OUT)
        GPIO.setup(self.left_servo_pin_nr, GPIO.OUT)

        self.right_servo_pin = GPIO.PWM(self.right_servo_pin_nr, 50)
        self.left_servo_pin = GPIO.PWM(self.left_servo_pin_nr, 50)

        self.right_servo_pin.start(self.initial_position)
        self.left_servo_pin.start(self.initial_position)

    def move(self, flaps):
        x = flaps["x"]
        y = flaps["y"]

        try:
            self.right_servo_pin.ChangeDutyCycle(float(x))
            self.left_servo_pin.ChangeDutyCycle(float(y))

        except KeyboardInterrupt:
            self.right_servo_pin.stop()
