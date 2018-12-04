import RPi.GPIO as GPIO


class FlapsService:

    def __init__(self):
        self.right_servo_pin = None
        self.right_servo_pin_nr = 12
        self.left_servo_pin = None
        self.left_servo_pin_nr = 11
        self.initial_position = 6
        self.__setup_module()
        self.MAX_MOVE = 12
        self.period = 20
        self.contra_positions = {
            '1': 11.0,
            '2': 10.0,
            '3': 9.0,
            '4': 8.0,
            '5': 7.0,
            '6': 6.0,
            '7': 5.0,
            '8': 4.0,
            '9': 3.0,
            '10': 2.0,
            '11': 1.0
        }

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
            self.left_servo_pin.stop()
