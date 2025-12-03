'''Third day's code for Advent of Code 2025.'''
import src.help as h
from src.day_03.power_bank import PowerBank


def main(input_path):
    '''Main function for day 3 challenge'''
    data = h.read_input(input_path)
    power_banks = [PowerBank(item) for item in data]
    total_joltage_p1 = sum(pb.two_bat_joltage for pb in power_banks)
    total_joltage_p2 = sum(pb.twelve_bat_joltage for pb in power_banks)
    return total_joltage_p1, total_joltage_p2


if __name__ == "__main__":
    print("Welcome to the third day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_03/example.txt")
    part1_puzzle, part2_puzzle = main("src/day_03/puzzle.txt")

    print(f"Total joltage part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    print(f"Total joltage part 1 (PUZZLE): {part1_puzzle}")
    print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
