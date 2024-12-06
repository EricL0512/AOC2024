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
    print(rule_list)
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
    print(total)


# PART TWO REQUIRES SOME GREEDY ALGORITHM OR INSIGHT
# INSIGHT FOUND!
def part_two():
    rule_list = []
    pattern_list = []
    wrong_patterns = []
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
        if not correct_pattern:
            wrong_patterns.append(pattern)

    # Brute force using two for loops
    # Yea that's not happening. 2^17 is too much permutations
    """IDEA: Make a list/dict/map based on the rules given? compare the pattern to the 
    list/dict/map and if its in ascending order then its correct? 

    To do this, find the front-most number based on the right side of the rule: FRONT MOST
    SHOULD NEVER BE ON THE RIGHT SIDE OF THE RULE AS ITS THE FIRST ELEMENT

    NVM this is alot easier than it looks:
    Find all possible values from both sides combined: use a set
    order values by how their mode/frequency of appearance on the right side of the rule
    this will be your guidance list/dict/map that will dictate how the rest of the lists are formed

    connect the pattern terms with the guidance list/dict/map 
    
    DOESNT WORK: RETRY
    """

    for line in wrong_patterns:
        pattern_found = False
        permutations = list(itertools.permutations(line))
        for line_two in permutations:
            correct_pattern = True
            for rule in rule_list:
                ahead = rule.split("|")[0]
                behind = rule.split("|")[1]
                if not (ahead in line_two and behind in line_two):
                    continue
                if line_two.index(behind) < line_two.index(ahead):
                    correct_pattern = False
            if correct_pattern:
                total += int(line_two[len(line_two) // 2])
                pattern_found = True
            if pattern_found:
                break


def redo_two():
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
    for behind in behind_list:
        if behind in rules_dict:
            rules_dict[behind] += 1
            print(rules_dict)
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
        correct_patterns = [''] * 50  # I believe its 49 total values but will put 50 to be safe
        for number in line:
            print(number)
            print(rules_dict[number])
            correct_patterns[rules_dict[number]] = number
            print(correct_patterns)
        temp_list = [i for i in correct_patterns if i != '']
        correct_patterns = temp_list
        print(correct_patterns)
        total += int(correct_patterns[len(correct_patterns) // 2])
    print(rules_dict)


file_data = get_file_data("input")
redo_two()
