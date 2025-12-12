'''Tenth day of Advent of Code 2025'''
import src.help as h
from src.day_10.machine import Machine


def main(input_path):
    '''Main function for day 9 challenge'''
    machines_data = h.read_input(input_path)
    machines = []
    for line in machines_data:
        machines.append(Machine(line))
    part1 = 0
    part2 = 0
    return part1, part2


if __name__ == '__main__':
    print("Welcome to the ninth day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_10/example.txt")
    # part1_puzzle, part2_puzzle = main("src/day_10/puzzle.txt")

    print(f"Largest area part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    # print(f"Largest area part 1 (PUZZLE): {part1_puzzle}")
    # print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
