import json

import tornado.ioloop
import tornado.web
import tornado.websocket

from modules.range_sensor import DistanceMeasureService


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()

    distance_sensor = DistanceMeasureService()

    def open(self):
        self.connections.add(self)

    def on_message(self, message):
        print(message)
        if message == "distance":
            distance = self.distance_sensor.measure_distance()

            msg = {"distance": distance}

            [client.write_message(json.dumps(msg)) for client in self.connections]

    [client.write_message("No command found") for client in self.connections]


def on_close(self):
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
