import tornado.ioloop
import tornado.web
import tornado.websocket


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SimpleWebSocket(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        self.connections.add(self)

    def on_message(self, message):
        print(message)
        [client.write_message(message) for client in self.connections]

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
