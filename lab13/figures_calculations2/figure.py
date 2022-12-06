from abc import ABC, abstractmethod


class Figure(ABC):
    coords = None

    def __init__(self, coords):
        self.coords = coords

    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_r(self):
        pass

    @abstractmethod
    def calc_R(self):
        pass
