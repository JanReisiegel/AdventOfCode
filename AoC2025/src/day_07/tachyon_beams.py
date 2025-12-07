'''Class for Tachyon Beams problem'''
from pprint import pprint


class TachyonBeams:
    '''Class for Tachyon Beams problem.'''

    def __init__(self, grid: list[list[str]]) -> None:
        self.grid = grid

    def split_times(self) -> int:
        '''Solves part 1 of the Tachyon Beams problem.'''
        result = 0
        # Implementation for solving part 1 goes here
        row_number = len(self.grid)
        col_number = len(self.grid[0])
        s_index = self.grid[0].index('S')
        self.grid[1][s_index] = '|'
        print(col_number, row_number)
        new_grid = [self.grid[i] for i in range(0, row_number, 2)]
        row_number = len(new_grid)
        for r in range(1, row_number):
            for c in range(col_number):
                if new_grid[r][c] == '^':
                    new_grid[r][c-1] = "|"
                    new_grid[r][c+1] = "|"
                    if new_grid[r-1][c] == '|' or new_grid[r-1][c] == 'S':
                        result += 1
        return result
