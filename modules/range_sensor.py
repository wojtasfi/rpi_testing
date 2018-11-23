import time

import RPi.GPIO as GPIO


class DistanceMeasureService:

    def __init__(self):
        self.TRIG = 23
        self.ECHO = 24
        self.ECHO_LOW = 0
        self.ECHO_HIGH = 1
        self.SOUND_SPEED_TWO_DIRECTIONS = 17150
        self.__setup_module()

    def __setup_module(self):
        GPIO.setmode(GPIO.BCM)

        print("Distance Measurement In Progress")

        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)

        GPIO.output(self.TRIG, False)
        print("Waiting For Sensor To Settle")
        time.sleep(2)

    def __send_signal(self):
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

    def measure_distance(self) -> int:
        self.__send_signal()

        while GPIO.input(self.ECHO) == self.ECHO_LOW:
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == self.ECHO_HIGH:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * self.SOUND_SPEED_TWO_DIRECTIONS
        distance = round(distance, 2)
        print("pulse_start:", pulse_start)
        print("pulse_end:", pulse_end)
        print("pulse_duration:", pulse_duration)
        print("Distance:", distance, "cm")
        return distance

    # GPIO.cleanup()
