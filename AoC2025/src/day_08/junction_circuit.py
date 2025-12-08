'''Class for the junction circuit on day 8'''
from src.day_08.junction_box import JunctionBox


class JunctionCircuit:
    '''Class representing a junction circuit'''
    def __init__(self, boxes: list[JunctionBox]) -> None:
        self.boxes = boxes

    def add_box(self, box: JunctionBox) -> None:
        '''Add a junction box to the circuit'''
        self.boxes.append(box)

    def distance_to(self, other: 'JunctionBox') -> float:
        '''Calculate the distance to another junction circuit'''
        tmp_distance = float('inf')
        for box in self.boxes:
            distance = box.distance_to(other)
            if distance < tmp_distance:
                tmp_distance = distance
        return tmp_distance

    def __str__(self):
        result = "JunctionCircuit with boxes:\n"
        for box in self.boxes:
            result += f"  {box}\n"
        return result
