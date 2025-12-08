'''Class for the junction circuit on day 8'''
from src.day_08.junction_box import JunctionBox


class JunctionCircuit:
    '''Class representing a junction circuit'''
    def __init__(self, boxes: list[JunctionBox]) -> None:
        self.boxes = boxes

    def add_box(self, box: JunctionBox) -> None:
        '''Add a junction box to the circuit'''
        self.boxes.append(box)

    def __contains__(self, box: JunctionBox) -> bool:
        return box in self.boxes

    def __len__(self) -> int:
        return len(self.boxes)

    def __str__(self):
        result = "JunctionCircuit with boxes:\n"
        for box in self.boxes:
            result += f"  {box}\n"
        return result
