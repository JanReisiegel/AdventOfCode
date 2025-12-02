'''Module for handling ID ranges'''
from src.day_02.id_card import IdCard


class IdRange:
    '''Class for storing all ID ranges'''
    def __init__(self, range_str: str):
        ranges = range_str.split('-')
        start_id = int(ranges[0])
        end_id = int(ranges[1])
        self.ids = []
        for number in range(start_id, end_id+1):
            self.ids.append(IdCard(number))

    def check_all_ids(self) -> int:
        '''This function checks all IDs in the range
        with the given check function'''
        count_p1 = 0
        count_p2 = 0
        for c_id in self.ids:
            part1_valid, part2_valid = c_id.is_valid()
            if not part1_valid:
                count_p1 += c_id.id_number  
            if not part2_valid:
                count_p2 += c_id.id_number

        return count_p1, count_p2

    def __str__(self) -> str:
        return f"IdRange({self.ids[0]}-{self.ids[-1]})"

    def __repr__(self) -> str:
        return f"IdRange(start_id={self.ids[0]}, end_id={self.ids[-1]})"
