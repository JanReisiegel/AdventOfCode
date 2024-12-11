'''Advent of code 2024 day 10 part 1 and 2'''
from collections import deque
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
HELP_DICTIONARY = {}


def worker_1(matrix, row, col):
    '''Worker function for part 1'''
    col_length = len(matrix[0])
    row_length = len(matrix)
    ans = 0
    seen = set()
    queue = deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if matrix[r][c] == 0:
            ans += 1
        for dir_row, dir_col in DIRECTIONS:
            result_row = r + dir_row
            result_col = c + dir_col
            if (
                0 <= result_row < row_length and
                0 <= result_col < col_length and
                matrix[result_row][result_col] == matrix[r][c] - 1
            ):
                queue.append((result_row, result_col))
    return ans


def worker_2(matrix, row, col):
    '''Worker function for part 2'''
    col_length = len(matrix[0])
    row_length = len(matrix)
    if matrix[row][col] == 0:
        return 1
    if (row, col) in HELP_DICTIONARY:
        return HELP_DICTIONARY[(row, col)]
    ans = 0
    for dir_row, dir_col in DIRECTIONS:
        result_row = row + dir_row
        result_col = col + dir_col
        if (
            0 <= result_row < row_length and
            0 <= result_col < col_length and
            matrix[result_row][result_col] == matrix[row][col] - 1
        ):
            ans += worker_2(matrix, result_row, result_col)
    HELP_DICTIONARY[(row, col)] = ans
    return ans


def main(file_path):
    '''Main function'''
    matrix = []
    part_1 = 0
    part_2 = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
        matrix = [[int(x) for x in row] for row in data]
        file.close()
    x_length = len(matrix[0])
    y_length = len(matrix)
    for row in range(y_length):
        for col in range(x_length):
            if matrix[row][col] == 9:
                part_1 += worker_1(matrix, row, col)
                HELP_DICTIONARY.clear()
                part_2 += worker_2(matrix, row, col)
    return part_1, part_2


if __name__ == '__main__':
    EXAMPLE_1, EXAMPLE_2 = main('10/example.txt')
    PART_1, PART_2 = main('10/puzzle.txt')
    print('Example part 1:', EXAMPLE_1)
    print('Part 1:', PART_1)
    print('Example part 2:', EXAMPLE_2)
    print('Part 2:', PART_2)
