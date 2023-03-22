from typing import Tuple

class Screen:
    dimensions: 'Tuple[float,float]'

    def __init__(self, dimensions: 'Tuple[float,float]'):
        self.dimensions = dimensions

    def to_absolute(self, point: 'Tuple[float,float]'):
        return (point[0] * self.dimensions[0], point[1] * self.dimensions[1])