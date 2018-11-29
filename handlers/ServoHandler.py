from modules.servo import ServoService


class ServoHandler:
    servo = ServoService()

    def handle(self, command, clients):
        self.servo.move(command)

    def get_command_name(self):
        return "servo"
