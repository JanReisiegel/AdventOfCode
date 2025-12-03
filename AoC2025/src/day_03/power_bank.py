'''Class representing a power bank for storing energy.'''
import itertools


class PowerBank:
    '''A power bank that can store energy using batteries.'''
    def __init__(self, batteries: str):
        '''Initialize the power bank with a given capacity.'''
        self.batteries = [int(battery) for battery in batteries]
        self.two_bat_joltage = self.calculate_two_bat_joltage()
        self.twelve_bat_joltage = self.calculate_twelve_bat_joltage()

    def calculate_two_bat_joltage(self) -> int:
        '''Calculate the best joltage configuration for the power bank.'''
        tmp_battery = 0
        max_joltage = 0
        batteries_len = len(self.batteries)
        for i in range(0, batteries_len):
            tmp_battery = self.batteries[i]
            for j in range(i+1, batteries_len):
                tmp_joltage = int(f"{tmp_battery}{self.batteries[j]}")
                if tmp_joltage > max_joltage:
                    max_joltage = tmp_joltage
        return max_joltage

    def calculate_twelve_bat_joltage(self) -> int:
        '''Calculate the best joltage configuration for twelve batteries.'''
        joltages = []
        joltages_tuples = itertools.permutations(self.batteries, 12)
        print(len(joltages_tuples))
        joltages = [1, 0]
        return max(joltages)

    def generate_indices(self, n, k, start_index, current_combination, results):
        '''Rekurzivně generuje kombinace 'k' indexů, 
        které musí být ve vzestupném pořadí.'''
        if k == 0:
            results.append(current_combination)
            return
        max_index = n - k
        for i in range(start_index, max_index + 1):
            self.generate_indices(
                n,
                k - 1,
                i + 1,
                current_combination + (i,),
                results
            )

    def __str__(self):
        return f'PowerBank(batteries={self.batteries})'
