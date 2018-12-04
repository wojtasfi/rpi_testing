from handlers.Handler import Handler
from modules.FlapsService import FlapsService


class FlapsHandler(Handler):
    flaps = FlapsService()

    def handle(self, command, clients):
        self.flaps.move(command)

    def get_command_name(self):
        return "flaps"
