from serviceable import Serviceable
from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Engine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self):
        self.battery = Battery()
        self.engine = Engine()

    def needs_service(self) -> bool:
        # Service is needed if either the battery or the engine needs service
        return self.battery.needs_service() or self.engine.needs_service()
