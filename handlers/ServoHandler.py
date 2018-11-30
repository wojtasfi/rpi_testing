from handlers.Handler import Handler
from modules.ServoService import ServoService


class ServoHandler(Handler):
    servo = ServoService()

    def handle(self, command, clients):
        self.servo.move(command)

    def get_command_name(self):
        return "servo"
