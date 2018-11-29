from modules.servo import ServoService


class ContinuousServoHandler:
    servo = ServoService()

    def handle(self, command, clients):
        self.servo.move(command)

    def get_command_name(self):
        return "continuous_servo"
