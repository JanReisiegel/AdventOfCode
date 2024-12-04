'''Advent of Code day 4 part 1 and 2'''


def check_direction_part_1(matrix, word, r, c, dr, dc):
    '''Check the direction of the word'''
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(len(word) - 1):
        nr, nc = r + i * dr, c + i * dc
        if not (0 <= nr < rows and 0 <= nc < cols):
            return False
        if matrix[nr][nc] != word[i]:
            return False
    return True


def worker_part_1(file_path: str) -> int:
    '''Work on the input file'''
    word = 'XMAS'
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as f:
        my_input = f.read()
        lines = my_input.split('\n')
        for line in lines:
            matrix.append(line)
        f.close()
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (-1, 1),  # Up-Right
        (-1, -1),  # Up-Left
        (-1, 0)   # Up
    ]
    result = 0
    rows, cols = len(matrix), len(matrix[0])
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction_part_1(matrix, word, r, c, dr, dc):
                    result += 1
    return result


if __name__ == "__main__":
    print(worker_part_1(file_path='04/example1.txt'))
    # print(worker_part_2(file_path='input.txt'))
