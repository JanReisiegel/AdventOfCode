'''Advent of code 2024 day 11 part 1 and 2'''
import time
TEMP_RESULT = {}


class Stone:
    '''Class to handle the stones'''
    def __init__(self, value):
        self.value = int(value)


class Stones:
    '''Class to handle the stones'''

    def __init__(self, values):
        print(values)
        self.stones = [Stone(value) for value in values]

    def blinking(self, number_of_blinkings):
        '''Blinking the stones'''
        for i in range(number_of_blinkings):
            if i % 10 == 0:
                print("Blink for the", i, "time")
            temp_array = []
            for stone in self.stones:
                stone_value = stone.value
                if stone_value == 0:
                    new_stone = Stone(1)
                    temp_array.append(new_stone)
                elif len(str(stone_value)) % 2 == 0:
                    left_stone = Stone(str(stone_value)
                                       [:int(len(str(stone_value))/2)])
                    right_stone = Stone(str(stone_value)
                                        [int(len(str(stone_value))/2):])
                    temp_array.append(left_stone)
                    temp_array.append(right_stone)
                else:
                    new_stone = Stone(stone_value*2024)
                    temp_array.append(new_stone)
            self.stones = temp_array
        return len(self.stones)


def worker(file_path):
    '''Worker function for part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        values = file.read().strip().split(' ')
        file.close()
        part_1 = Stones(values)
        part_2 = Stones(values)
        start_part_1 = time.time()
        result_1 = part_1.blinking(25)
        time_part_1 = time.time() - start_part_1
        print('Time part 1:', time_part_1)
        start_part_2 = time.time()
        result_2 = part_2.blinking(75)
        time_part_2 = time.time() - start_part_2
        print('Time part 2:', time_part_2)
    return result_1, result_2


if __name__ == '__main__':
    EXAMPLE_1, EXAMPLE_2 = worker('11/example.txt')
    PART_1, PART_2 = worker('11/puzzle.txt')
    print('Example part 1:', EXAMPLE_1)
    print('Part 1:', PART_1)
    print('Example part 2:', EXAMPLE_2)
    print('Part 2:', PART_2)
