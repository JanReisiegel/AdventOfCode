'''Second day's challenge of Advent of Code 2025.'''
import src.help as h
from src.day_02.id_range import IdRange


def main(input_path):
    '''Main function for day 2 challenge'''
    data = h.read_input_splited(input_path, delimiter=',')
    total_valid_ids_p1 = 0
    total_valid_ids_p2 = 0
    for item in data:
        id_range = IdRange(item)
        count_p1, count_p2 = id_range.check_all_ids()
        total_valid_ids_p1 += count_p1
        total_valid_ids_p2 += count_p2

    return total_valid_ids_p1, total_valid_ids_p2


if __name__ == "__main__":
    print("Welcome to the second day of 12 Days of Code 2025!")
    valid_ids_example_p1, valid_ids_example_p2 = main("src/day_02/example.txt")
    valid_ids_puzzle_p1, valid_ids_puzzle_p2 = main("src/day_02/puzzle.txt")

    print(f"The number of valid IDs (EXAMPLE, Part 1): {valid_ids_example_p1}")
    print(f"The number of valid IDs (PUZZLE, Part 1): {valid_ids_puzzle_p1}")

    print("-"*40)

    print(f"The number of valid IDs (EXAMPLE, Part 2): {valid_ids_example_p2}")
    print(f"The number of valid IDs (PUZZLE, Part 2): {valid_ids_puzzle_p2}")
