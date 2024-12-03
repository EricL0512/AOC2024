import re
from typing import TextIO


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def part_one():
    total = 0
    for line in file_data:
        list = line.split("mul")
        list.pop(0)
        for string in list:
            if string[0] == "(" and ")" in string:
                string = string[1:string.find(")")]
                if len(string.split(",")) == 2:
                    first = string.split(",")[0]
                    second = string.split(",")[1]
                    if first.isnumeric() and second.isnumeric():
                        total += int(first) * int(second)
    print(f"part two: {total}")


def part_two():
    all_lines = ""
    total = 0
    for line in file_data:
        all_lines += line
    all_lines = re.sub(r"don't\(\).+?do\(\)", "", all_lines)  # I HATE GREEDY ALGORITHMS
    all_lines = re.sub(r"don't\(\).+", "", all_lines)
    list = all_lines.split("mul")
    list.pop(0)
    for string in list:
        if string[0] == "(" and ")" in string:
            string = string[1:string.find(")")]
            if len(string.split(",")) == 2:
                first = string.split(",")[0]
                second = string.split(",")[1]
                if first.isnumeric() and second.isnumeric():
                    total += int(first) * int(second)
    print(f"part one: {total}")


file_data = get_file_data("input")
part_one()
part_two()
