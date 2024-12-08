'''Advent of Code 2024 day 7 part 1 and 2'''


class Calibration:
    '''Calibration class'''

    def __init__(self, line_data):
        '''Init'''
        parsed_line = line_data.split(': ')
        self.result = int(parsed_line[0])
        self.equations = [int(number) for number in parsed_line[1].split(' ')]

    def __str__(self):
        '''String representation'''
        return f'{self.result} = {self.equations}'

    def evaluate(self, numbers, operators):
        '''Evaluate expression'''
        result = numbers[0]
        len_operators = len(operators)
        for i in range(len_operators):
            if operators[i] == '+':
                result += numbers[i+1]
            else:
                result = result * numbers[i+1]
        return result

    def is_calibrated(self, numbers=None, part_2=False):
        '''Check if calibration is calibrated'''
        target = self.result
        numbers = self.equations if numbers is None else numbers
        if len(numbers) == 1:
            return numbers[0] == target
        if self.is_calibrated([numbers[0] + numbers[1]] + numbers[2:], part_2):
            return True
        if self.is_calibrated([numbers[0] * numbers[1]] + numbers[2:], part_2):
            return True
        if part_2 and self.is_calibrated([int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], part_2): # noqa
            return True
        return False


def calibrations_result(calibrations, part_2=False):
    '''Calculate calibration result'''
    result = []
    for calibration in calibrations:
        if calibration.is_calibrated(part_2=part_2):
            result.append(calibration.result)
    return result


def worker_part_1(file_path):
    '''Worker part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
        calibrations = [Calibration(line) for line in lines]
        file.close()
    result = calibrations_result(calibrations)
    return sum(result) if result else 0


def worker_part_2(file_path):
    '''Worker part 2'''
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
        calibrations = [Calibration(line) for line in lines]
        file.close()
    result = calibrations_result(calibrations, True)
    return sum(result) if result else 0


if __name__ == '__main__':
    print('Example part 1:', worker_part_1('07/example1.txt'))
    print('Part 1:', worker_part_1('07/puzzle1.txt'))
    print('Example part 2:', worker_part_2('07/example1.txt'))
    print('Part 2:', worker_part_2('07/puzzle1.txt'))
