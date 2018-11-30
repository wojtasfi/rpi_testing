from handlers.Handler import Handler
from modules.ContinuousServoService import ContinuousServoService


class ContinuousServoHandler(Handler):
    servo = ContinuousServoService()

    def handle(self, command, clients):
        self.servo.move(command)

    def get_command_name(self):
        return "continuous_servo"
