'''First day of AoC 2024'''


class Location:
    '''Class to store the location of the elves'''
    def __init__(self, left_id=0, right_id=0):
        self.left_id = left_id
        self.right_id = right_id

    def get_distance(self):
        '''Get the distance between the two locations'''
        return abs(self.left_id - self.right_id)


def split_input(my_input):
    '''Split the input into a list of strings'''
    lines = my_input.split('\n')
    locations = []
    for i in range(len(lines)):
        line = lines[i].split()
        locations.append(Location(int(line[0]), int(line[1])))
    return locations


if __name__ == "__main__":
    with open('01/example1.txt') as f:
        my_input = f.read()
        print(my_input)
        print(split_input(my_input))
        f.close()
