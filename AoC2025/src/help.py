'''file with helper functions for AoC 2025 challenges '''


def read_input(file_path) -> list[str]:
    """Reads the input file and returns its content as a list of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def read_input_splited(file_path, delimiter=',') -> list[str]:
    """Reads the input file and splits its content by the given delimiter."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        return content.split(delimiter)


def read_input_two_arrays(file_path, delimiter='') -> tuple[list[str],
                                                            list[str]]:
    """Reads the input file and splits its content into two arrays based
    on a delimiter line."""
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
        file.close()
    split_index = lines.index(delimiter)
    return lines[:split_index], lines[split_index + 1:]


def read_input_to_matrix(file_path) -> list[list[str]]:
    """Reads the input file and returns content as a matrix (list of lists)."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return [[char for char in line.strip()] for line in file.readlines()]


def write_output(file_path, data):
    """Writes the given data to the output file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(f"{line}\n")
