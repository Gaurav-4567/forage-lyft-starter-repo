from abc import ABC, abstractmethod
from datetime import date

from car import Car


class CarFactory(ABC):
    @abstractmethod
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        pass

    @abstractmethod
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        pass

    @abstractmethod
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        pass

    @abstractmethod
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int) -> Car:
        pass

    @abstractmethod
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int) -> Car:
        pass
