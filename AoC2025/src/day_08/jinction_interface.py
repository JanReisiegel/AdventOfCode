'''Interface for junction boxes and circuits on day 8'''
from typing import Protocol
from src.day_08.junction_box import JunctionBox


class JunctionInterface(Protocol):
    '''Abstract base class for junction components'''
    def distance_to(self, other: 'JunctionBox') -> float:
        '''Calculate the distance to another junction component'''
