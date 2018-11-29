from handlers.ContinuousDistanceHandler import ContinuousDistanceHandler
from handlers.DistanceHandler import DistanceHandler
from handlers.ServoHandler import ServoHandler


class HandlersSupplier:

    def __init__(self):
        self.handlers = [DistanceHandler(), ContinuousDistanceHandler(), ServoHandler()]

    def handle_command(self, message, clients):

        print("Message to handle")
        print(message)
        command_name = message.command_name
        command = message.command

        for handler in self.handlers:
            if handler.get_command_name() == command_name:
                return handler.handle(command, clients)
