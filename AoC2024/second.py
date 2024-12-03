'''Advent of Code 2024, Day 2, Part 1 & 2'''


class Report:
    '''Class to handle the report'''
    def __init__(self, numbers):
        self.numbers = [int(number) for number in numbers]

    def get_status(self) -> int:
        '''Get the status of the report
        1 for: The levels are either all increasing or all decreasing.
            Any two adjacent levels differ by at least one and at most three.
        0 for: The levels are not all increasing or all decreasing.'''
        # Check if the levels are increasing or decreasing
        increasing_or_decreasing = (self.numbers == sorted(self.numbers) or
                                    self.numbers == sorted(self.numbers,
                                                           reverse=True))
        result = True
        for i in range(len(self.numbers) - 1):
            difference = abs(self.numbers[i + 1] - self.numbers[i])
            if not 1 <= difference <= 3:
                result = False
                break
        return int(increasing_or_decreasing and result)

    def get_second_status(self) -> int:
        '''Get the status of the report
        1 for: The levels are either all increasing or all decreasing.
            Any two adjacent levels differ by at least one and at most three.
        0 for: The levels are not all increasing or all decreasing.'''
        # Check if the levels are increasing or decreasing
        result = False
        for i in range(len(self.numbers)):
            temp = self.numbers[:i] + self.numbers[i + 1:]
            good = self.is_good(temp)
            # print(temp, self.numbers, good)
            if good:
                result = True
        # print(result, self.numbers)
        return int(result)

    def is_good(self, numbers):
        '''Check if the numbers are good'''
        good = True
        increasing_or_decreasing = (numbers == sorted(numbers) or numbers ==
                                    sorted(numbers, reverse=True))
        for j in range(len(numbers) - 1):
            difference = abs(numbers[j] - numbers[j + 1])
            if not 1 <= difference <= 3:
                good = False
                break
        return good and increasing_or_decreasing


def split_content_part_1(content):
    '''Split the content into a list of strings'''
    reports = []
    lines = content.split('\n')
    for line in lines:
        numbers = line.split()
        report = Report(numbers)
        reports.append(report.get_status())
    return sum(reports)


def worker_part_1(file_path):
    '''Work on the input file'''
    result = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        result = split_content_part_1(content=data)
        f.close()
    return result


def split_content_part_2(content):
    '''Split the content into a list of strings'''
    reports = []
    lines = content.split('\n')
    for line in lines:
        numbers = line.split()
        report = Report(numbers)
        reports.append(report.get_second_status())
    return sum(reports)


def worker_part_2(file_path):
    '''Work on the input file'''
    result = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        result = split_content_part_2(content=data)
        f.close()
    return result


if __name__ == '__main__':
    example_1 = worker_part_1('02/example1.txt')
    print('Example 1:', example_1)
    part_1 = worker_part_1('02/puzzle1.txt')
    print('Part 1:', part_1)
    example_2 = worker_part_2('02/example1.txt')
    print('Example 2:', example_2)
    part_2 = worker_part_2('02/puzzle1.txt')
    print('Part 2:', part_2)
