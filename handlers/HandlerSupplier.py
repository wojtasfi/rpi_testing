from handlers.ContinuousDistanceHandler import ContinuousDistanceHandler
from handlers.DistanceHandler import DistanceHandler


class HandlersSupplier:

    def __init__(self):
        self.handlers = [DistanceHandler(), ContinuousDistanceHandler()]

    def handle_command(self, message, clients):
        command_name = message.command_name
        command = message.command

        for handler in self.handlers:
            if handler.get_command_name() == command_name:
                return handler.handle(command, clients)
