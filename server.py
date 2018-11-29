import json

import RPi.GPIO as GPIO
import tornado.ioloop
import tornado.web
import tornado.websocket

from handlers import HandlerSupplier


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    GPIO.cleanup()
    connections = set()

    handlerSupplier = HandlerSupplier.HandlersSupplier()

    def open(self):
        print("Connection open")
        self.connections.add(self)

    # message = {command_name:"", command: ""}
    def on_message(self, message):
        self.handlerSupplier.handle_command(message=json.parse(message), clients=self.connections)

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
