'''Seventh day of Advent of Code 2025'''
import src.help as h
from src.day_07.tachyon_beams import TachyonBeams


def main(input_path):
    '''Main function for day 7 challenge'''
    problems = h.read_input_to_matrix(input_path)
    tachyon_beams = TachyonBeams(problems)
    part1 = tachyon_beams.split_times()
    part2 = 0
    return part1, part2


if __name__ == '__main__':
    print("Welcome to the seventh day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_07/example.txt")
    part1_puzzle, part2_puzzle = main("src/day_07/puzzle.txt")

    print(f"Total joltage part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    print(f"Total joltage part 1 (PUZZLE): {part1_puzzle}")
    print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
