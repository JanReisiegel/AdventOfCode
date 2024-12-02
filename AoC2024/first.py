'''First day of AoC 2024'''


class Location:
    '''Class to store the location of the elves'''
    def __init__(self, left_id=0, right_id=0):
        self.left_id = left_id
        self.right_id = right_id

    def get_distance(self):
        '''Get the distance between the two locations'''
        return abs(self.left_id - self.right_id)

    def __str__(self):
        return f'{self.left_id} {self.right_id}'


def split_input_part_1(my_input):
    '''Split the input into a list of strings'''
    lines = my_input.split('\n')
    left_ids = []
    right_ids = []
    locations = []
    for line in lines:
        new_line = line.split()
        left_ids.append(int(new_line[0]))
        right_ids.append(int(new_line[1]))
    # seřadí left_ids a right_ids od nejmenšího po největší
    left_ids.sort()
    right_ids.sort()
    for left_id in left_ids:
        locations.append(Location(left_id, right_ids.pop(0)))
    return locations


def worker_part_1(file_path):
    '''Work on the input file'''
    locations = []
    result = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        my_input = f.read()
        locations = split_input_part_1(my_input=my_input)
        f.close()
    for location in locations:
        result += location.get_distance()
    return result


def split_input_part_2(my_input):
    '''Split the input into a list of strings'''
    lines = my_input.split('\n')
    left_ids = []
    right_ids = []
    results = []
    for line in lines:
        new_line = line.split()
        left_ids.append(int(new_line[0]))
        right_ids.append(int(new_line[1]))
    for left_id in left_ids:
        number = right_ids.count(left_id)
        results.append(left_id * number)
    return sum(results)


def worker_part_2(file_path):
    '''Work on the input file'''
    result = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        my_input = f.read()
        result = split_input_part_2(my_input=my_input)
        f.close()
    return result


if __name__ == "__main__":
    example1 = worker_part_1('01/example1.txt')
    print(f'Example 1: {example1}')
    part1 = worker_part_1('01/puzzle1.txt')
    print(f'Part 1: {part1}')
    example2 = worker_part_2('01/example1.txt')
    print(f'Example 2: {example2}')
    part2 = worker_part_2('01/puzzle1.txt')
    print(f'Part 2: {part2}')
