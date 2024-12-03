'''Advent of Code 2024, Day 3, Part 1 & 2'''
import re


class Multiply:
    '''Class to multiply two numbers'''
    def __init__(self, a, b):
        '''Initialize the class with two numbers'''
        self.a = a
        self.b = b

    def multiply(self):
        '''Return the product of two numbers'''
        return self.a * self.b


def worker_1(file_path):
    '''Read the input file and return the product of two numbers'''
    multiply_strings = []
    result = []
    with open(file_path, 'r', encoding='utf-8') as file:
        multiply_strings = re.findall(r'mul\(\d{1,3},\d{1,3}\)', file.read())
        file.close()
    for string in multiply_strings:
        a, b = re.findall(r'\d{1,3}', string)
        multiply_numbers = Multiply(int(a), int(b))
        result.append(multiply_numbers.multiply())
    return sum(result)


def worker_2(file_path):
    '''Read the input file and return the product of two numbers'''
    multiply_strings = []
    result = []
    with open(file_path, 'r', encoding='utf-8') as file:
        multiply_strings = re. \
            findall(r'do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)', file.read())
        file.close()
    enabled = True
    for string in multiply_strings:
        if string == 'do()':
            enabled = True
        elif string == 'don\'t()':
            enabled = False
        elif "mul" in string and enabled:
            a, b = re.findall(r'\d{1,3}', string)
            multiply_numbers = Multiply(int(a), int(b))
            result.append(multiply_numbers.multiply())
    # print(multiply_strings)
    return sum(result)


if __name__ == '__main__':
    m = Multiply(3, 5)
    print(m.multiply())
    example_1 = worker_1('03/example1.txt')
    print('Example 1:', example_1)
    part1 = worker_1('03/puzzle1.txt')
    print('Part 1:', part1)
    example_2 = worker_2('03/example2.txt')
    print('Example 2:', example_2)
    part2 = worker_2('03/puzzle1.txt')
    print('Part 2:', part2)
