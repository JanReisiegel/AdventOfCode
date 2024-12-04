'''Advent of Code day 4 part 1 and 2'''


def word_calculator_part_1(matrix, word) -> int:
    '''Calculet the number of words in the matrix'''
    rows = len(matrix)
    result = 0
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if (
                j + 3 < cols and
                matrix[i][j] == word[0] and
                matrix[i][j+1] == word[1] and
                matrix[i][j+2] == word[2] and
                matrix[i][j+3] == word[3]
            ):
                result += 1
            if (
                j + 3 < cols and
                matrix[i][j] == word[3] and
                matrix[i][j+1] == word[2] and
                matrix[i][j+2] == word[1] and
                matrix[i][j+3] == word[0]
            ):
                result += 1
            if (
                i + 3 < rows and
                matrix[i][j] == word[0] and
                matrix[i+1][j] == word[1] and
                matrix[i+2][j] == word[2] and
                matrix[i+3][j] == word[3]
            ):
                result += 1
            if (
                i + 3 < rows and
                matrix[i][j] == word[3] and
                matrix[i+1][j] == word[2] and
                matrix[i+2][j] == word[1] and
                matrix[i+3][j] == word[0]
            ):
                result += 1
            if (
                i + 3 < rows and
                j + 3 < cols and
                matrix[i][j] == word[0] and
                matrix[i+1][j+1] == word[1] and
                matrix[i+2][j+2] == word[2] and
                matrix[i+3][j+3] == word[3]
            ):
                result += 1
            if (
                i + 3 < rows and
                j + 3 < cols and
                matrix[i][j] == word[3] and
                matrix[i+1][j+1] == word[2] and
                matrix[i+2][j+2] == word[1] and
                matrix[i+3][j+3] == word[0]
            ):
                result += 1
            if (
                i - 3 >= 0 and
                j + 3 < cols and
                matrix[i][j] == word[0] and
                matrix[i-1][j+1] == word[1] and
                matrix[i-2][j+2] == word[2] and
                matrix[i-3][j+3] == word[3]
            ):
                result += 1
            if (
                i - 3 >= 0 and
                j + 3 < cols and
                matrix[i][j] == word[3] and
                matrix[i-1][j+1] == word[2] and
                matrix[i-2][j+2] == word[1] and
                matrix[i-3][j+3] == word[0]
            ):
                result += 1
    return result


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
    result = word_calculator_part_1(matrix, word)          
    return result


def word_calculator_úart_2(matrix, word):
    '''Calculate the number of words in the matrix'''
    cols, rows = len(matrix[0]), len(matrix)
    result = 0
    for i in range(rows):
        for j in range(cols):
            if (
                i + 2 < rows and
                j + 2 < cols and
                matrix[i][j] == word[0] and
                matrix[i+1][j+1] == word[1] and
                matrix[i+2][j+2] == word[2] and
                matrix[i+2][j] == word[0] and
                matrix[i][j+2] == word[2]
            ):
                result += 1
            if (
                i + 2 < rows and
                j + 2 < cols and
                matrix[i][j] == word[0] and
                matrix[i+1][j+1] == word[1] and
                matrix[i+2][j+2] == word[2] and
                matrix[i+2][j] == word[2] and
                matrix[i][j+2] == word[0]
            ):
                result += 1
            if (
                i + 2 < rows and
                j + 2 < cols and
                matrix[i][j] == word[2] and
                matrix[i+1][j+1] == word[1] and
                matrix[i+2][j+2] == word[0] and
                matrix[i+2][j] == word[0] and
                matrix[i][j+2] == word[2]
            ):
                result += 1
            if (
                i + 2 < rows and
                j + 2 < cols and
                matrix[i][j] == word[2] and
                matrix[i+1][j+1] == word[1] and
                matrix[i+2][j+2] == word[0] and
                matrix[i+2][j] == word[2] and
                matrix[i][j+2] == word[0]
            ):
                result += 1
    return result


def worker_part_2(file_path: str) -> int:
    '''Work on the input file'''
    word = 'MAS'
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as f:
        my_input = f.read()
        matrix = my_input.split('\n')
        f.close()
    result = word_calculator_úart_2(matrix, word)
    return result


if __name__ == "__main__":
    print('Example part 1:', worker_part_1(file_path='04/example1.txt'))
    print('Part 1:', worker_part_1(file_path='04/puzzle1.txt'))
    print('Example part 2:', worker_part_2(file_path='04/example1.txt'))
    print('Part 2:', worker_part_2(file_path='04/puzzle1.txt'))
