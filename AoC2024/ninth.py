'''Advent of code 2024 day 9 part 1 and 2'''


class FileSystem:
    '''Class for file system'''

    def __init__(self, input_line):
        '''Initiate file system'''
        self.disk = []
        self.moved_disk = []
        self.blocks = [int(x) for x in input_line]

    def disk_map(self):
        '''Create disk map'''
        free_space = False
        block_id = 0
        for number in self.blocks:
            change_id = False
            for i in range(number):
                if free_space:
                    self.disk.append('.')
                else:
                    self.disk.append(block_id)
                    change_id = True
            if change_id:
                block_id += 1
            free_space = not free_space

    def move_blocks(self):
        '''Move blocks'''
        for disk_part_1 in self.disk:
            pass
        


def worker_1(file_path):
    '''Worker for part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        line = file.read().strip()
        file.close()
    fs = FileSystem(line)
    fs.disk_map()
    return 1


if __name__ == '__main__':
    print('Example part 1:', worker_1('09/example.txt'))
    # print('Part 1:', worker_1('09/puzzle.txt'))
