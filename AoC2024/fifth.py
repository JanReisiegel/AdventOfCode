'''Advent of Code day 5 part 1 and 2'''
import math
from collections import defaultdict


class Rule:
    '''Rule class'''

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def get_numbers(self):
        '''Get the numbers from the rule'''
        return (self.first, self.second)

    def __str__(self):
        return f'{self.first}|{self.second}'


def rules_parser(rules_strings):
    '''Parse the rules'''
    rules = []
    for rule in rules_strings:
        rule = rule.split('|')
        rules.append(Rule(int(rule[0]), int(rule[1])))
    return rules


def updates_parser(updates_strings):
    '''Parse the updates'''
    updates = []
    for update in updates_strings:
        update = update.split(',')
        updates.append([int(x) for x in update])
    return updates


def updates_evaluator_part_1(updates, rules) -> int:
    '''Evaluate the updates'''
    results = []
    for update in updates:
        update_result = 0
        used_rules = len(rules)
        for rule in rules:
            try:
                first_position = update.index(rule.first)
                second_position = update.index(rule.second)
            except ValueError:
                used_rules -= 1
                continue
            if first_position >= second_position:
                break
            update_result += 1
        if update_result == used_rules:
            results.append(update[math.floor(len(update)/2)])
    return sum(results)


def worker_part_1(file_path):
    '''Advent of Code day 5 part 1'''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
    data = data.split('\n\n')
    rules = rules_parser(data[0].split('\n'))
    updates = updates_parser(data[1].split('\n'))
    return updates_evaluator_part_1(updates, rules)


def updates_evaluator_part_2(updates, rules) -> int:
    '''Evaluate the updates'''
    results = []
    for update in updates:
        update_result = 0
        used_rules = len(rules)
        for rule in rules:
            try:
                first_position = update.index(rule.first)
                second_position = update.index(rule.second)
            except ValueError:
                used_rules -= 1
                continue
            if first_position >= second_position:
                update_result += 1
        if update_result > 0:
            repaired_update = repaire_update(update, rules)
            results.append(repaired_update[math.floor(len(repaired_update)/2)])
    return sum(results)


def repaire_update(update, rules):
    '''Repaire the update'''
    graph = defaultdict(set)
    for rule in rules:
        x, y = rule.get_numbers()
        graph[y].add(x)
    visited = set()
    repaired_update = []
    update_set = set(update)


    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor in update_set:
                visit(neighbor)
        repaired_update.append(node)

    for node in update:
        visit(node)
    return repaired_update


def worker_part_2(file_path):
    '''Advent of Code day 5 part 2'''
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        file.close()
    data = data.split('\n\n')
    rules = rules_parser(data[0].split('\n'))
    updates = updates_parser(data[1].split('\n'))
    return updates_evaluator_part_2(updates, rules)


if __name__ == '__main__':
    print('Example part 1:', worker_part_1('05/example1.txt'))
    print('Part 1:', worker_part_1('05/puzzle1.txt'))
    print('Example part 2:', worker_part_2('05/example1.txt'))
    print('Part 2:', worker_part_2('05/puzzle1.txt'))
