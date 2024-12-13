'''Adven of code 2024 day 12 part 1 and 2'''
from collections import deque
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
SEEN = set()


def calculate(matrix, row, col, row_len, col_len):
    '''Calculate the area and perimeter of the island'''
    if matrix[row][col] in SEEN:
        return 0
    queue = deque([(row, col)])
    area = 0
    perimeter = 0
    perimeter_dict = dict()
    while queue:
        r, c = queue.popleft()
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        area += 1
        for direction_row, direction_col in DIRECTIONS:
            result_row = r + direction_row
            result_col = c + direction_col
            if (
                0 <= result_row < row_len and
                0 <= result_col < col_len and
                matrix[result_row][result_col] == matrix[r][c]
            ):
                queue.append((result_row, result_col))
            else:
                perimeter += 1
                if (direction_row, direction_col) not in perimeter_dict:
                    perimeter_dict[(direction_row, direction_col)] = set()
                perimeter_dict[(direction_row, direction_col)].add((r, c))
    sides = 0
    for _, values in perimeter_dict.items():
        seen_perimeter = set()
        for (value_row, value_col) in values:
            if (value_row, value_col) not in seen_perimeter:
                sides += 1
                queue = deque([(value_row, value_col)])
                while queue:
                    r, c = queue.popleft()
                    if (r, c) in seen_perimeter:
                        continue
                    seen_perimeter.add((r, c))
                    for direction_row, direction_col in DIRECTIONS:
                        result_row = r + direction_row
                        result_col = c + direction_col
                        if (result_row, result_col) in values:
                            queue.append((result_row, result_col))
    return area * perimeter, area * sides


def worker(file_path):
    '''Worker function'''
    input_matrix = []
    result_1 = 0
    result_2 = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        input_matrix = file.read().split('\n')
        file.close()
    row_len = len(input_matrix)
    col_len = len(input_matrix[0])
    for row in range(row_len):
        for col in range(col_len):
            calculate_1, calculate_2 = calculate(input_matrix,
                                                 row, col, row_len, col_len)
            result_1 += calculate_1
            result_2 += calculate_2
    return result_1, result_2


if __name__ == "__main__":
    EXAMPLE_1_1, EXAMPLE_1_2 = worker("12/example_1.txt")
    EXAMPLE_2_1, EXAMPLE_2_2 = worker("12/example_2.txt")
    PART_1, PART_2 = worker("12/puzzle.txt")
    print('Example 1 part 1:', EXAMPLE_1_1)
    print('Example 2 part 1:', EXAMPLE_2_1)
    print('Part 1:', PART_1)
    print('Example 1 part 2:', EXAMPLE_1_2)
    print('Example 2 part 2:', EXAMPLE_2_2)
    print('Part 2:', PART_2)
