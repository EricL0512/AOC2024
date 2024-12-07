import itertools
from typing import TextIO


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


# Find ones already in right order

def part_one():
    rule_list = []
    pattern_list = []
    pattern_start = False
    total = 0
    # Separate the inputs
    for line in file_data:
        if line != "" and not pattern_start:
            rule_list.append(line)
        elif not pattern_start:
            pattern_start = True
        else:
            pattern_list.append(line)
    for pattern in pattern_list:
        correct_pattern = True
        pattern = pattern.split(',')
        for rule in rule_list:
            ahead = rule.split("|")[0]
            behind = rule.split("|")[1]
            if not (ahead in pattern and behind in pattern):
                continue
            if pattern.index(behind) < pattern.index(ahead):
                correct_pattern = False
        if correct_pattern:
            total += int(pattern[len(pattern) // 2])
    print(f"part_one: {total}")

# map usage to identify index of a string; then build out the list
# using a map to sort a list, then taking middle element
def part_two():
    rule_list = []
    pattern_list = []
    ahead_list = []
    behind_list = []
    wrong_patterns = []
    rules_dict: dict = {}
    pattern_start = False
    total = 0
    # Separate the inputs
    for line in file_data:
        if line != "" and not pattern_start:
            rule_list.append(line)
        elif not pattern_start:
            pattern_start = True
        else:
            pattern_list.append(line)
    # create the rules list, make the rules dict
    for rule in rule_list:
        ahead_list.append(rule.split("|")[0])
        behind_list.append(rule.split("|")[1])
    rule_list_nocopy = list(set(ahead_list + behind_list))
    for number in rule_list_nocopy:
        rules_dict[number] = 0

    # find wrong patterns
    for pattern in pattern_list:
        correct_pattern = True
        pattern = pattern.split(',')
        for rule in rule_list:
            ahead = rule.split("|")[0]
            behind = rule.split("|")[1]
            if not (ahead in pattern and behind in pattern):
                continue
            if pattern.index(behind) < pattern.index(ahead):
                correct_pattern = False
        if not correct_pattern:
            wrong_patterns.append(pattern)
    for line in wrong_patterns:
        for number in rules_dict:
            rules_dict[number] = 0
        for index in range(len(behind_list)):
            if (behind_list[index] in line) and (ahead_list[index] in line) and (behind_list[index] in rules_dict):
                rules_dict[behind_list[index]] += 1
        correct_patterns = [''] * 50  # I believe its 49 total values but will put 50 to be safe
        for number in line:
            correct_patterns[rules_dict[number]] = number
        temp_list = [i for i in correct_patterns if i != '']
        correct_patterns = temp_list
        total += int(correct_patterns[len(correct_patterns) // 2])
    print(f"part two: {total}")


file_data = get_file_data("input")
part_one()
part_two()
