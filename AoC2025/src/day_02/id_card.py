'''Module for validating ID cards.'''
import re


class IdCard:
    '''Class for storing and validating an ID card'''
    def __init__(self, id_number: int):
        self.id_number = id_number

    def is_valid(self) -> bool:
        """Check if the ID number is valid based on a simple checksum rule."""
        id_str = str(self.id_number)
        search_invalid_p1 = re.search(r'^(.+)\1$', id_str)
        search_invalid_p2 = re.search(r'^(.+)\1+$', id_str)
        part1, part2 = True, True
        if search_invalid_p1:
            # print(f"Part 1 invalid ID found: {self.id_number} (matches: {search_invalid_p1.group(0)})")
            part1 = False
        if search_invalid_p2:
            # print(f"Part 2 invalid ID found: {self.id_number} (matches: {search_invalid_p2.group(0)})")
            part2 = False
        return part1, part2

    def __str__(self) -> str:
        return f"IdCard({self.id_number})"
