'''Class for the machine used in Day 10.'''
import re


class Machine:
    '''Class for the machine used in Day 10.'''

    def __init__(self, line: str) -> None:
        temp_patern = re.match(r"^\[(\.?[\.#]+\.?)\]", line).group(1)
        self.light_pattern = [1 if char == '#' else 0 for char in temp_patern]
        N = len(self.light_pattern)
        self.instructions = []
        temp_instructions = re.findall(r"\((.*?)\)", line)
        for instr in temp_instructions:
            parts = [int(i.strip()) for i in instr.split(',') if i.strip()]
            button = [0]*N
            for i in parts:
                button[i] = 1 if 0 <= i < N else 0
            self.instructions.append(button)
        joltage_parts = re.findall(r"\{([^\}]+)\}", line)[0].split(',')
        self.joltage = [int(j) for j in joltage_parts]
