from handlers.ContinuousDistanceHandler import ContinuousDistanceHandler
from handlers.ContinuousServoHandler import ContinuousServoHandler
from handlers.DistanceHandler import DistanceHandler
from handlers.FlapsHandler import FlapsHandler


class HandlersSupplier:

    def __init__(self):
        self.handlers = [DistanceHandler(),
                         ContinuousDistanceHandler(),
                         # ServoHandler(), for flaps testing
                         ContinuousServoHandler(),
                         FlapsHandler()]

    def handle_command(self, message, clients):

        print("Message to handle")
        print(message)
        command_name = message.command_name
        command = message.command

        for handler in self.handlers:
            if handler.get_command_name() == command_name:
                return handler.handle(command, clients)
