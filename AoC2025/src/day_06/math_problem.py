'''Class for math problems.'''


class MathProblem:
    '''Class for math problems.'''

    def __init__(self, problem: list[list[str]]) -> None:
        self.problems = problem

    def solve1(self) -> int:
        '''Solves part 1 of the math problem.'''
        result = 0
        # Implementation for solving part 1 goes here
        len_problem = len(self.problems[0])
        len_problems = len(self.problems) - 1
        for i in range(len_problem):
            if self.problems[-1][i] == '+':
                for j in range(len_problems):
                    result += int(self.problems[j][i])
            elif self.problems[-1][i] == '*':
                prod = 1
                for j in range(len_problems):
                    prod *= int(self.problems[j][i])
                result += prod
            else:
                result += 0
        return result
    
    def solve2(self) -> int:
        '''Solves part 2 of the math problem.'''
        result = 0
        # Implementation for solving part 2 goes here
        len_problem = len(self.problems[0])
        len_problems = len(self.problems) - 1
        return result
