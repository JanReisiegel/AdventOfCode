'''Eighth day of Advent of Code 2025'''
import src.help as h
from src.day_08.junction_circuit import JunctionCircuit
from src.day_08.junction_box import JunctionBox


def main(input_path):
    '''Main function for day 8 challenge'''
    coords = h.read_input(input_path)
    boxes = [JunctionBox(coord.split(',')) for coord in coords]
    all_best_distance = []
    circuits = []
    for box in boxes:
        print(box)
        distances = []
        for other_box in boxes:
            if box != other_box:
                distances.append((box, other_box, box.distance_to(other_box)))
        distances.sort(key=lambda x: x[2])
        all_best_distance.append(distances[0])      
    print("All best distances:")
    for entry in all_best_distance:
        print(f"From {entry[0]} to {entry[1]}: {entry[2]:.2f}")
    number_boxes = len(boxes)
    while len(circuits) < number_boxes:
        
    part1 = 0
    part2 = 0
    return part1, part2


if __name__ == '__main__':
    print("Welcome to the eighth day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_08/example.txt")
    # part1_puzzle, part2_puzzle = main("src/day_08/puzzle.txt")

    print(f"Total joltage part 1 (EXAMPLE): {part1_example}")
    print(f"Total joltage part 2 (EXAMPLE): {part2_example}")

    print("-"*40)

    # print(f"Total joltage part 1 (PUZZLE): {part1_puzzle}")
    # print(f"Total joltage part 2 (PUZZLE): {part2_puzzle}")
