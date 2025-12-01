'''file with helper functions for AoC 2025 challenges '''


def read_input(file_path):
    """Reads the input file and returns its content as a list of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
