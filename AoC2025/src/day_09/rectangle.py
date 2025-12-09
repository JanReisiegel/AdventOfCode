'''Class for rectangles in day 9 challenge'''


class Rectangle:
    '''Class for rectangles in day 9 challenge'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        '''Calculate the area of the rectangle'''

        return abs((max(self.x) + 1 - min(self.x)) *
                   (max(self.y) + 1 - min(self.y)))
