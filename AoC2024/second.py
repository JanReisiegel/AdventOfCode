class Report:
    '''Class to handle the report'''
    def __init__(self, numbers):
        self.numbers = numbers

    def get_status(self) -> int:
        '''Get the status of the report'''
        if int(self.numbers[0]) == int(self.numbers[1]):
            return 0
        report_type = int(self.numbers[0]) < int(self.numbers[1])
        if report_type:
            for i in range(0, len(self.numbers)-2):
                if int(self.numbers[i]) > int(self.numbers[i+1]):
                    return 0
                elif int(self.numbers[i+1]) == int(self.numbers[i]):
                    return 0
                elif int(self.numbers[i+1])-int(self.numbers[i]) > 3:
                    return 0
                else:
                    continue
        else:
            for i in range(0, len(self.numbers)-2):
                if int(self.numbers[i]) < int(self.numbers[i+1]):
                    return 0
                elif int(self.numbers[i])-int(self.numbers[i+1]) > 3:
                    return 0
                elif int(self.numbers[i+1]) == int(self.numbers[i]):
                    return 0
                else:
                    continue
        return 1


def split_content_part_1(content):
    '''Split the content into a list of strings'''
    reports = []
    lines = content.split('\n')
    for line in lines:
        numbers = line.split()
        report = Report(numbers)
        reports.append(report.get_status())
    return sum(reports)


def worker_part_1(file_path):
    '''Work on the input file'''
    result = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        result = split_content_part_1(content=data)
        f.close()
    return result


if __name__ == '__main__':
    example_1 = worker_part_1('02/example1.txt')
    print('Example 1:', example_1)
    part_1 = worker_part_1('02/puzzle1.txt')
    print('Part 1:', part_1)
