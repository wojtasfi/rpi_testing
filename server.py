import json
import time

import RPi.GPIO as GPIO
import tornado.ioloop
import tornado.web
import tornado.websocket

from modules.range_sensor import DistanceMeasureService


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    GPIO.cleanup()
    connections = set()

    distance_sensor = DistanceMeasureService()
    distance_continuous = False

    def open(self):
        print("Connection open")
        self.connections.add(self)

    def on_message(self, message):
        print(message)
        if message == "distance":
            distance = self.distance_sensor.measure_distance()
            msg = {"distance": distance}
            [client.write_message(json.dumps(msg)) for client in self.connections]

        elif message == "distance_continuous":
            self.distance_continuous = True

            while self.distance_continuous:
                distance = self.distance_sensor.measure_distance()
                msg = {"distance": distance}
                [client.write_message(json.dumps(msg)) for client in self.connections]
                time.sleep(0.02)

        elif message == "distance_continuous_stop":
            self.distance_continuous = False

        else:
            [client.write_message("No command found") for client in self.connections]

    def on_close(self):
        print("Connection closed")
        self.connections.remove(self)

    # todo not secure
    def check_origin(self, origin):
        return True


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/websocket", SimpleWebSocket)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
