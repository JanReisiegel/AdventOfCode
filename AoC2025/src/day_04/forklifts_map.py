'''Class to represent a map of forklifts and their movements.'''
import numpy as np


class ForkliftsMap:
    '''Forklifts map representation.'''
    def __init__(self, matrix_input: list[list[str]]):
        self.map = matrix_input

    def how_can_accessed(self, symbol) -> int:
        '''How many rolls can be accessed by forklifts.'''
        tmp_map = np.pad(self.map,
                         pad_width=1,
                         mode='constant',
                         constant_values='.')
        map_length = len(tmp_map)
        map_width = len(tmp_map[0])
        count = 0
        for i in range(1, map_length-1):
            for j in range(1, map_width-1):
                if tmp_map[i][j] == symbol:
                    tmp_mini_map = tmp_map[i-1:i+2, j-1:j+2]
                    rolls_count = np.sum(
                        (tmp_mini_map == symbol) | (tmp_mini_map == 'x')) - 1
                    if rolls_count < 4:
                        count += 1
                        tmp_map[i][j] = 'x'
        return count

    def how_can_accessed_v2(self, symbol) -> int:
        '''How many rolls can be accessed by forklifts - version 2.'''
        tmp_map = np.pad(self.map,
                         pad_width=1,
                         mode='constant',
                         constant_values='.')
        map_length = len(tmp_map)
        map_width = len(tmp_map[0])
        count = 0
        access = True
        while access:
            access = False
            for i in range(1, map_length-1):
                for j in range(1, map_width-1):
                    if tmp_map[i][j] == symbol:
                        tmp_mini_map = tmp_map[i-1:i+2, j-1:j+2]
                        rolls_count = np.sum(
                            (tmp_mini_map == symbol) |
                            (tmp_mini_map == 'x')) - 1
                        if rolls_count < 4:
                            count += 1
                            tmp_map[i][j] = 'x'
            if np.any(tmp_map == 'x'):
                access = True
            tmp_map[tmp_map == 'x'] = '.'
        return count

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map])
