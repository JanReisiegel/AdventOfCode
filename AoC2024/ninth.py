'''Advent of code 2024 day 9 part 1 and 2'''


class FileSystem:
    '''Class for file system'''

    def __init__(self, input_line):
        '''Initiate file system'''
        self.disk = []
        self.moved_disk = []
        self.checksum = []
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
        with open('09/disk.txt', 'w', encoding='utf-8') as file:
            file.write('[\'' + '\',\''.join(map(str, self.disk)) + '\']')
            file.close()
        # print(self.disk)

    def move_blocks(self):
        '''Move blocks'''
        disk_len = len(self.disk)
        last_index = disk_len - 1
        for i in range(disk_len):
            if i > last_index:
                break
            if self.disk[i] != '.':
                self.moved_disk.append(self.disk[i])
                self.checksum.append(self.disk[i] * i)
                continue
            not_inserted = True
            while not_inserted:
                if self.disk[last_index] == '.':
                    last_index -= 1
                else:
                    self.moved_disk.append(self.disk[last_index])
                    self.checksum.append(self.disk[last_index] * i)
                    last_index -= 1
                    not_inserted = False
        with open('09/moved_disk.txt', 'w', encoding='utf-8') as file:
            file.write('[\'' + '\',\''.join(map(str, self.moved_disk)) + '\']')
            file.close()


def worker_1(file_path):
    '''Worker for part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        line = file.read().strip()
        file.close()
    fs = FileSystem(line)
    fs.disk_map()
    # print(fs.disk)
    fs.move_blocks()
    # print(fs.moved_disk)
    return sum(fs.checksum)


if __name__ == '__main__':
    print('Example part 1:', worker_1('09/example.txt'))
    print('Part 1:', worker_1('09/puzzle.txt'))
