import json

from handlers import Handler
from modules.range_sensor import DistanceMeasureService


class DistanceHandler(Handler):
    distance_sensor = DistanceMeasureService()

    def handle(self, command, clients):
        distance = self.distance_sensor.measure_distance()
        msg = {"distance": distance}
        [client.write_message(json.dumps(msg)) for client in clients]

    def get_command_name(self):
        return "distance"
