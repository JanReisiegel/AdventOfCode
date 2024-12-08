'''Advent of code 2024 day 8 part 1 and 2'''
from collections import defaultdict


def prepare_frequencies(lines):
    '''Prepare frequencies'''
    frequencies = defaultdict(list)
    x_length = len(lines)
    y_length = len(lines[0])
    for i in range(x_length):
        for j in range(y_length):
            if lines[i][j] != '.':
                frequencies[lines[i][j]].append((i, j))
    return frequencies


def calculate_impact_worker(lines, frequencies):
    '''Calculate impact worker'''
    x_length = len(lines)
    y_length = len(lines[0])
    result_1 = set()
    result_2 = set()
    for x in range(x_length):
        for y in range(y_length):
            for k, vs in frequencies.items():
                for (x1, y1) in vs:
                    for (x2, y2) in vs:
                        if (x1, y1) != (x2, y2):
                            d1 = abs(x - x1) + abs(y - y1)
                            d2 = abs(x - x2) + abs(y - y2)
                            dx1 = x - x1
                            dy1 = y - y1
                            dx2 = x - x2
                            dy2 = y - y2
                            if (
                                (d1 == 2*d2 or d1*2 == d2) and
                                (0 <= x < x_length) and
                                0 <= y < y_length and
                                (dx1 * dy2 == dy1 * dx2)
                            ):
                                result_1.add((x, y))
                            if (
                                (0 <= x < x_length) and
                                (0 <= y < y_length) and
                                (dx1 * dy2 == dy1 * dx2)
                            ):
                                result_2.add((x, y))
    return len(result_1), len(result_2)


def calculate_impact(lines):
    '''Calculate impact 1'''
    frequencies = prepare_frequencies(lines)
    result = calculate_impact_worker(lines, frequencies)
    return result


def worker(file_path):
    '''Worker part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
        file.close()
    result = calculate_impact(lines)
    return result


if __name__ == '__main__':
    EXAMPLE_1, EXAMPLE_2 = worker('08/example.txt')
    print('Example part 1:', EXAMPLE_1)
    PART_1, PART_2 = worker('08/puzzle1.txt')
    print('Part 1:', PART_1)
    print('Example part 2:', EXAMPLE_2)
    print('Part 2:', PART_2)
