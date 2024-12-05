import random
from typing import TextIO
import itertools

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
            if not(ahead in pattern and behind in pattern):
                continue
            if pattern.index(behind) < pattern.index(ahead):
                correct_pattern = False
        if correct_pattern:
            total += int(pattern[len(pattern) // 2])
    print(total)

# PART TWO REQUIRES SOME GREEDY ALGORITHM OR INSIGHT
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
    O(n)? 
    """
    
    
    print(wrong_patterns)
    for line in wrong_patterns:
        pattern_found = False
        permutations = list(itertools.permutations(line))
        print(permutations)
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
    print(total)


file_data = get_file_data("input")
perm = list(itertools.permutations(
    ['94', '76', '47', '44', '18', '87', '86', '95', '84', '35', '74', '73', '68', '19', '42', '15', '65']))
print(perm)
