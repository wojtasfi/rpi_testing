import json
import time

from handlers.Handler import Handler
from modules.range_sensor import DistanceMeasureService


class ContinuousDistanceHandler(Handler):
    distance_sensor = DistanceMeasureService()

    def __init__(self):
        self.measure_on = False

    def handle(self, command, clients):
        if command == "start":
            self.measure_on = True
            print("Starting measuring distance")

            while self.measure_on:
                distance = self.distance_sensor.measure_distance()
                msg = {"distance": distance}
                [client.write_message(json.dumps(msg)) for client in clients]
                time.sleep(0.02)

        elif command == "stop":
            print("Stopping measuring distance")
            self.measure_on = False

    def get_command_name(self):
        return "distance_continuous"
