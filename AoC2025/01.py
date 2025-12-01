'''First day of 12 Days of Code 2025'''
from src import help as h

def main(input_path, start=50):
    current_value = start
    operations = h.read_input(input_path)
    part1 = 0
    part2 = 0
    for op in operations:
        direction = op[0]
        value = int(op[1:])
        zero_flag = 0
        if input_path == "01/puzzle01.txt":
            print(value)
        if direction == 'R':
            current_value, part2_plus = right_turn(current_value, value)
        elif direction == 'L':
            current_value, part2_plus = left_turn(current_value, value)
        if current_value == 0:
            part1 += 1
    return part1, part2


def normalize_value(value):
    value = value % 100
    return value


def left_turn(current_value, turn_value):
    new_value = current_value - turn_value
    return normalize_value(new_value)


def right_turn(current_value, turn_value):
    new_value = current_value + turn_value
    return normalize_value(new_value)


if __name__ == "__main__":
    print("Welcome to the first day of 12 Days of Code 2025!")
    part1_test, part2_test = main("01/puzzle01.txt")
    print(f"The result after all operations is (TEST Part1): {part1_test}")
    part1_real, part2_real = main("01/puzzle1.txt")
    print(f"The result after all operations is (PUZZLE Part1): {part1_real}")
    print("-" * 40)
    print(f"The number of times we hit 0 (TEST Part2): {part2_test}")
    print(f"The number of times we hit 0 (PUZZLE Part2): {part2_real}")