'''Class to manage ingredients database'''


class IngredientsDatabase:
    '''Ingredients database representation.'''
    def __init__(self, ranges, available_ids):
        self.ranges = []
        self.ranges2 = []
        for r in ranges:
            parts = r.split('-')
            self.ranges2.append((int(parts[0]), int(parts[1])))
            self.ranges.append(range(int(parts[0]), int(parts[1])+1))
        self.ranges2.sort(key=lambda x: x[0])
        self.available_ids = [int(i) for i in available_ids]

    def count_fresh_ingredients(self) -> int:
        '''Count fresh ingredients based on ID ranges.'''
        count = 0
        for ingredient_id in self.available_ids:
            if any(ingredient_id in r for r in self.ranges):
                count += 1
        return count

    def count_fresh_ingredients_ranges(self) -> int:
        '''Count fresh ingredients using an optimized approach.'''
        merged_ranges = []
        # print(self.ranges2)
        count = 0
        actual_range = (0, 0)
        for next_range in self.ranges2:
            if actual_range[1] < next_range[0]:
                if actual_range != (0, 0):
                    count += actual_range[1] - actual_range[0] + 1
                    merged_ranges.append(actual_range)
                actual_range = next_range
            elif actual_range[1] >= next_range[0]:
                actual_range = (actual_range[0], max(actual_range[1],
                                                     next_range[1]))
        merged_ranges.append(actual_range)
        count += actual_range[1] - actual_range[0] + 1
        return count
