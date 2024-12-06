'''Advent of Code 2024, Day 6, Part 1'''
from collections import deque


class Map:
    '''Map class'''

    def __init__(self, data: str):
        temp_data = data.split("\n")
        self.data = []
        self.seen = []
        self.seen_rc = []
        for row in temp_data:
            self.data.append(list(row))
        self.direction = '^'

    def go(self) -> bool:
        '''Go about 1 position forward'''
        x, y = self.find_position(self.direction)
        self.data[y][x] = 'X'
        if self.direction == '^':
            y -= 1
        elif self.direction == 'v':
            y += 1
        elif self.direction == '<':
            x -= 1
        elif self.direction == '>':
            x += 1

        self.turn_right(x, y)

        if (0 <= x < len(self.data[0])) and (0 <= y < len(self.data)):
            self.data[y][x] = self.direction
            return False
        return True

    def go_2(self):
        '''Go about 1 position forward'''
        result = 0
        p1 = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                r, c = self.find_position(self.direction)
                direction = 0
                while True:
                    if (r, c, direction) in self.seen:
                        result += 1
                        break
                    self.seen.append((r, c, direction))
                    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
                    rr = r+dr
                    cc = c+dc
                    if not (0 <= rr < len(self.data) and 0 <= cc <
                            len(self.data[0])):
                        if self.data[y][x]=='#':
                            p1 = len(self.seen_rc)
                        break
                    if self.data[rr][cc] == '#' or rr == y and cc == x:
                        direction = (direction+1) % 4
                    else:
                        r = rr
                        c = cc
        print(p1)
        return result

    def find_position(self, char: str):
        '''Find position of char'''
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == char:
                    return x, y
        return None

    def turn_right(self, x, y):
        '''Turn right'''
        try:
            if self.direction == '^' and self.data[y-1][x] == '#':
                self.direction = '>'
            elif self.direction == '>' and self.data[y][x+1] == '#':
                self.direction = 'v'
            elif self.direction == 'v' and self.data[y+1][x] == '#':
                self.direction = '<'
            elif self.direction == '<' and self.data[y][x-1] == '#':
                self.direction = '^'
        except IndexError:
            return

    def calculate_visited(self) -> int:
        '''Calculate visited distincts'''
        visited = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == 'X':
                    visited += 1
        return visited


def worker_path_1(file_path: str) -> int:
    '''Returns number of visited distincts'''
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        my_map = Map(data)
        f.close()
    is_out = False
    while not is_out:
        is_out = my_map.go()
    return my_map.calculate_visited()


def worker_path_2(file_path: str) -> int:
    '''Returns number of visited distincts'''
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        my_map = Map(data)
        f.close()
    result = my_map.go_2()
    return result


if __name__ == "__main__":
    print('Example part 1:', worker_path_1("06/example1.txt"))
    print('Part 1:', worker_path_1("06/puzzle1.txt"))
    print('Example part 2:', worker_path_2("06/example1.txt"))
