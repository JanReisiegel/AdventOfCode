'''Eighth day of Advent of Code 2025'''
import math
import src.help as h
from src.day_08.junction_circuit import JunctionCircuit
from src.day_08.junction_box import JunctionBox


def main(input_path):
    '''Main function for day 8 challenge'''
    coords = h.read_input(input_path)
    boxes = [JunctionBox(coord.split(',')) for coord in coords]
    distances = []
    boxes_len = len(boxes)
    for i in range(boxes_len-2):
        box = boxes[i]
        for j in range(i+1, boxes_len):
            other_box = boxes[j]
            dist = box.distance_to(other_box)
            if box != other_box and (other_box, box, dist) not in distances:
                distances.append((box, other_box, dist))
    distances.sort(key=lambda x: x[2])
    part1 = 0
    part2 = 0
    if "example.txt" in input_path:
        part1, part2 = solve(distances, 10)
    else:
        part1, part2 = solve(distances, 1000)
    return part1, part2


def solve(distances, iterations):
    '''Solve the example input'''
    it = 0
    circuits = []
    while it < iterations:
        box = distances[it][0]
        shortest = distances[it][1]
        box_circuit = None
        shortest_circuit = None
        for circuit in circuits:
            if box in circuit:
                box_circuit = circuit
            if shortest in circuit:
                shortest_circuit = circuit
        if box_circuit and shortest_circuit:
            if box_circuit != shortest_circuit:
                box_circuit.boxes.extend(shortest_circuit.boxes)
                circuits.remove(shortest_circuit)
        elif box_circuit:
            box_circuit.add_box(shortest)
        elif shortest_circuit:
            shortest_circuit.add_box(box)
        else:
            new_circuit = JunctionCircuit([box, shortest])
            circuits.append(new_circuit)
        it += 1
    circuits.sort(key=len, reverse=True)
    part1 = math.prod([len(circuits[i]) for i in range(3)])
    return part1, 0


if __name__ == '__main__':
    print("Welcome to the eighth day of 12 Days of Code 2025!")
    part1_example, part2_example = main("src/day_08/example.txt")

    print(f"Total product part 1 (EXAMPLE): {part1_example}")
    print(f"Total product part 2 (EXAMPLE): {part2_example}")

    print("-"*40)
    part1_puzzle, part2_puzzle = main("src/day_08/puzzle.txt")

    print(f"Total product part 1 (PUZZLE): {part1_puzzle}")
    print(f"Total product part 2 (PUZZLE): {part2_puzzle}")
