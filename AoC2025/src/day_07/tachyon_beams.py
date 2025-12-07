'''Class for Tachyon Beams problem'''


class TachyonBeams:
    '''Class for Tachyon Beams problem.'''

    def __init__(self, grid: list[list[str]]) -> None:
        self.grid = grid

    def split_times(self) -> int:
        '''Solves part 1 of the Tachyon Beams problem.'''
        result = 0
        # Implementation for solving part 1 goes here
        row_number = len(self.grid)-1
        col_number = len(self.grid[0])
        for i in range(row_number):
            for j in range(col_number):
                if self.grid[i][j] == 'S':
                    self.grid[i+1][j] = '|'
        return result
