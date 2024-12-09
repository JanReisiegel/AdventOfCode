'''Advent of code 2024 day 9 part 1 and 2'''
from collections import deque


class FileSystem:
    '''Class for file system'''

    def __init__(self, input_line):
        '''Initiate file system'''
        self.checksum_1 = []
        self.checksum_2 = []
        self.blocks = [int(x) for x in input_line]

    def disk_map(self):
        '''Create disk map'''
        disk_1 = deque([])
        disk_2 = deque([])
        space = deque([])
        file_id = 0
        position = 0
        for i, c in enumerate(self.blocks):
            if i % 2 == 0:
                disk_2.append((position, int(c), file_id))
                for i in range(int(c)):
                    self.checksum_1.append(file_id)
                    self.checksum_2.append(file_id)
                    disk_1.append((position, 1, file_id))
                    position += 1
            else:
                space.append((position, int(c)))
                for i in range(int(c)):
                    self.checksum_1.append(None)
                    self.checksum_2.append(None)
                    position += 1
        for (position, size, file_id) in reversed(disk_1):
            for space_i, (space_position, space_size) in enumerate(space):
                if space_position < position and size <= space_size:
                    for i in range(size-1):
                        assert self.checksum_1[position + i] == file_id, \
                            f'{self.checksum_1[position + i]=}'
                        self.checksum_1[position + i] = None
                        self.checksum_1[space_position + i] = file_id
                    space[space_i] = (space_position + size, space_size - size)
                    break
        for (position, size, file_id) in reversed(disk_2):
            for space_i, (space_position, space_size) in enumerate(space):
                if space_position < position and size <= space_size:
                    for i in range(size-1):
                        assert self.checksum_2[position + i] == file_id, \
                            f'{self.checksum_2[position + i]=}'
                        self.checksum_2[position + i] = None
                        self.checksum_2[space_position + i] = file_id
                    space[space_i] = (space_position + size, space_size - size)
                    break
        result_1 = 0
        result_2 = 0
        for i, c in enumerate(self.checksum_1):
            if c is not None:
                result_1 += i * c
        for i, c in enumerate(self.checksum_2):
            if c is not None:
                result_2 += i * c
        return result_1, result_2


def worker(file_path):
    '''Worker for part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        line = file.read().strip()
        file.close()
    fs = FileSystem(line)
    result = fs.disk_map()
    return result


if __name__ == '__main__':
    example_1, example_2 = worker('09/example.txt')
    part_1, part_2 = worker('09/puzzle.txt')
    print('Example part 1:', example_1)
    print('Part 1:', part_1)
    print('Example part 2:', example_2)
    print('Part 2:', part_2)
