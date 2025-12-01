'''file with helper functions for AoC 2025 challenges '''


def read_input(file_path):
    """Reads the input file and returns its content as a list of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def write_output(file_path, data):
    """Writes the given data to the output file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(f"{line}\n")
