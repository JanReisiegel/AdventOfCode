'''Sixth day of Advent of Code 2025'''
import src.help as h
from src.day_06.math_problem import MathProblem


def main(input_path):
    '''Main function for day 6 challenge'''
    problems = h.read_input_to_strings_matrix(input_path)
    math_problem = MathProblem(problems)
    part1 = math_problem.solve1()
    part2 = 0
    return part1, part2


if __name__ == '__main__':
    print("Welcome to the sixth day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_06/example.txt")
    part1_puzzle, part2_puzzle = main("src/day_06/puzzle.txt")

    print(f"Total joltage part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    print(f"Total joltage part 1 (PUZZLE): {part1_puzzle}")
    print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
