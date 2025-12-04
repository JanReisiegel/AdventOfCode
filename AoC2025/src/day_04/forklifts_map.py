'''Class to represent a map of forklifts and their movements.'''


class ForkliftsMap:
    '''Forklifts map representation.'''
    def __init__(self, input_data):
        self.map = []
        for line in input_data:
            self.map.append([line[i] for i in range(len(line))])
    
    def how_can_accessed(self, symbol) -> int:
        '''How many rolls can be accessed by forklifts.'''
        tmp_map = self.map.copy()
        map_length = len(tmp_map)
        map_width = len(tmp_map[0])
        for i in range(len(map_length)):
            for j in range(len(map_width)):
                tmp_mini_map = self.map[i-1:i+1][j-1:j+1]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map])
