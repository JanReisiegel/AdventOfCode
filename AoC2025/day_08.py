'''Eighth day of Advent of Code 2025'''
import src.help as h
from src.day_08.junction_circuit import JunctionCircuit
from src.day_08.junction_box import JunctionBox


def main(input_path):
    '''Main function for day 8 challenge'''
    coords = h.read_input(input_path)
    boxes = [JunctionBox(coord.split(',')) for coord in coords]
    count = 0
    while True:
        selected_box = boxes[0]
        tmp_distance = float('inf')
        result = None
        for box in boxes:
            if box == selected_box:
                continue
            print(f"Comparing {selected_box} to {box}")
            distance = selected_box.distance_to(box)
            print(f"Distance from {selected_box} to {box} is {distance}")
            if distance < tmp_distance:
                tmp_distance = distance
                result = box
        boxes.remove(selected_box)
        boxes.remove(result)
        boxes.insert(0, JunctionCircuit([selected_box, result]))
        print(f"Closest to {selected_box} is {result} "
              f"with distance {tmp_distance}")
        count += 1
        if count == 2:
            break
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
