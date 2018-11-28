from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def handle(self, command, clients):
        pass

    @abstractmethod
    def get_command_name(self):
        pass
