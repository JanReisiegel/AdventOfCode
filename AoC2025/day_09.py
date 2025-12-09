'''Ninth day of Advent of Code 2025'''
import src.help as h
from src.day_09.rectangle import Rectangle


def main(input_path):
    '''Main function for day 9 challenge'''
    points = h.read_input(input_path)
    areas = []
    len_points = len(points)
    for i in range(len_points):
        point_x = points[i].split(",")
        x1 = int(point_x[0])
        y1 = int(point_x[1])
        for j in range(i + 1, len_points):
            point_y = points[j].split(",")
            x2 = int(point_y[0])
            y2 = int(point_y[1])
            rect = Rectangle((x1, x2), (y1, y2))
            areas.append(rect.area())
    part1 = max(areas) if areas else 0
    part2 = 0
    return part1, part2


if __name__ == '__main__':
    print("Welcome to the ninth day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_09/example.txt")
    part1_puzzle, part2_puzzle = main("src/day_09/puzzle.txt")

    print(f"Largest area part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    print(f"Largest area part 1 (PUZZLE): {part1_puzzle}")
    print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
