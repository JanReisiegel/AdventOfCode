'''Class for the junction box on day 8'''
import math


class JunctionBox:
    '''Class representing a junction box'''
    def __init__(self, coords: list[str]) -> None:
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.z = int(coords[2])

    def distance_to(self, other: 'JunctionBox') -> float:
        '''Calculate the Euclidean distance to another junction box'''
        return math.sqrt(
            math.pow(self.x - other.x, 2) +
            math.pow(self.y - other.y, 2) +
            math.pow(self.z - other.z, 2)
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
