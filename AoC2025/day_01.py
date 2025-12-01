'''First day of 12 Days of AoC 2025'''
from src import help as h


def main(input_path, start=50):
    '''Main function for Day 1 of 12 Days of AoC 2025'''
    current_position = start
    operations = h.read_input(input_path)
    part1 = 0
    part2 = 0
    # results = []
    for op in operations:
        tmp_position = current_position
        direction = op[0]
        distance = int(op[1:])
        quotient, distance = divmod(distance, 100)
        part2 += quotient
        new_position = 0
        if direction == 'R':
            new_position = right_turn(current_position, distance)
        elif direction == 'L':
            new_position = left_turn(current_position, distance)
        quotient, current_position = divmod(new_position, 100)
        if all([quotient, tmp_position != 0, current_position != 0]):
            part2 += 1
        if current_position == 0:
            part1 += 1
            part2 += 1
    # h.write_output("01/output.txt", results)
    return part1, part2


def left_turn(current_value, turn_value):
    '''Perform a left turn operation'''
    new_value = current_value - turn_value
    return new_value


def right_turn(current_value, turn_value):
    '''Perform a right turn operation'''
    new_value = current_value + turn_value
    return new_value


if __name__ == "__main__":
    print("Welcome to the first day of 12 Days of Code 2025!")
    part1_test, part2_test = main("01/example.txt")
    print(f"The result after all operations is (TEST Part1): {part1_test}")
    part1_real, part2_real = main("01/puzzle.txt")
    print(f"The result after all operations is (PUZZLE Part1): {part1_real}")
    print("-" * 40)
    print(f"The number of times we hit 0 (TEST Part2): {part2_test}")
    print(f"The number of times we hit 0 (PUZZLE Part2): {part2_real}")
