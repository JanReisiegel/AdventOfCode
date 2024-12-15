'''Advent of code day 13 part 1 and 2'''
import re
from math import gcd
from sympy import diophantine, symbols, Eq, solve


class ClawMachine:
    '''Claw machine class'''
    def __init__(self, button_a, button_b, prize):
        self.cost_a = 3
        self.cost_b = 1
        x_a, y_a = re.findall(r'X\+(\d+)', button_a), \
            re.findall(r'Y\+(\d+)', button_a)
        x_b, y_b = re.findall(r'X\+(\d+)', button_b), \
            re.findall(r'Y\+(\d+)', button_b)
        x_prize, y_prize = re.findall(r'X=(\d+)', prize), \
            re.findall(r'Y=(\d+)', prize)
        self.button_a = (int(x_a[0]), int(y_a[0]))
        self.button_b = (int(x_b[0]), int(y_b[0]))
        self.prize = (int(x_prize[0]), int(y_prize[0]))
        self.best_tokens = self.get_costs(100), \
            self.get_costs_part_2(1000000000000)
        print('next machine')

    def get_costs(self, max_pushes_on_button):
        '''Get costs'''
        seen = {}
        for i in range(max_pushes_on_button):
            for j in range(max_pushes_on_button):
                if (i, j) in seen:
                    continue
                if (
                    i * self.button_a[0] + j * self.button_b[0] ==
                    self.prize[0] and
                    i * self.button_a[1] + j * self.button_b[1] ==
                    self.prize[1]
                ):
                    seen[(i, j)] = i * self.cost_a + j * self.cost_b
        if seen:
            return min(seen.values())
        else:
            return 0

    def get_costs_part_2(self, offset: int):
        '''Get costs part 2'''
        x_prize, y_prize = self.prize[0] + offset, \
            self.prize[1] + offset

        gcd_x = gcd(self.button_a[0], self.button_b[0])
        gcd_y = gcd(self.button_a[1], self.button_b[1])

        if x_prize % gcd_x != 0 or y_prize % gcd_y != 0:
            print('No solution')
            return 0

        x, y = symbols('x y', integer=True)

        eq_x = self.button_a[0] * x + self.button_b[0] * y
        eq_y = self.button_a[1] * x + self.button_b[1] * y
        print(eq_x, eq_y)

        solution_x = (eq_x)
        solution_y = (eq_y)
        valid_costs = []
        #print(f"Solutions for X-axis equation: {solution_x}")
        #print(f"Solutions for Y-axis equation: {solution_y}")
        for sxx, sxy in solution_x:
            for syx, syy in solution_y:
                if sxx == syx and sxy == syy:
                    cost = sxx * self.cost_a + sxy * self.cost_b
                    valid_costs.append(cost)
        result = min(valid_costs) if valid_costs else 0
        #print(result, valid_costs)
        return result


def worker(file_path):
    '''Worker function'''
    machines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = re.findall(r'Button A: .*\nButton B: .*\nPrize: .*',
                          file.read())
        file.close()
    for machine in data:
        button_a, button_b, prize = machine.split('\n')
        machines.append(ClawMachine(button_a, button_b, prize))
    return sum([machine.best_tokens[0] for machine in machines]), \
        sum([machine.best_tokens[1] for machine in machines])


if __name__ == '__main__':
    EXAMPLE_1, EXAMPLE_2 = worker('13/example.txt')
    print('----------------------------------------')
    PART_1, PART_2 = worker('13/puzzle.txt')
    print('Example part 1: ', EXAMPLE_1)
    print('Part 1: ', PART_1)
    print('Example part 2: ', EXAMPLE_2)
    print('Part 2: ', PART_2)
