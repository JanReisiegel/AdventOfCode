'''Class representing a power bank for storing energy.'''


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
        joltage = ""
        tmp_index = 0
        # print(self.batteries)
        for i in range(11, -1, -1):
            # print(self.batteries[tmp_index:len(self.batteries)-i], 
            # tmp_index, "-", len(self.batteries)-i, i)
            tmp_max = max(self.batteries[tmp_index:len(self.batteries)-i])
            joltage += str(tmp_max)
            # print(joltage)
            tmp_index = self.batteries[tmp_index:len(self.batteries)-i]. \
                index(tmp_max) + tmp_index + 1
        # print(self.batteries, joltage)
        # print("-"*40)
        return int(joltage)

    def __str__(self):
        return f'PowerBank(batteries={self.batteries})'
