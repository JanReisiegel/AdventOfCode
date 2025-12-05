'''Fifth day of Advent of Code 2025'''
import src.help as h
from src.day_05.ingredients_database import IngredientsDatabase


def main(input_path):
    '''Main function for day 5 challenge'''
    ranges, ids = h.read_input_two_arrays(input_path)
    ingredient_db = IngredientsDatabase(ranges, ids)
    part1 = ingredient_db.count_fresh_ingredients()
    part2 = ingredient_db.count_fresh_ingredients_ranges()
    return part1, part2


if __name__ == '__main__':
    print("Welcome to the fifth day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_05/example.txt")
    part1_puzzle, part2_puzzle = main("src/day_05/puzzle.txt")

    print(f"Total joltage part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    print(f"Total joltage part 1 (PUZZLE): {part1_puzzle}")
    print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
