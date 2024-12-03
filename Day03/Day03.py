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
    print(total)

def part_two():
    all_lines = ""
    total = 0
    for line in file_data:
        all_lines += line
    all_lines = re.sub(r"don't\(\).+do\(\)", "", all_lines)
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
    print(total)



file_data = get_file_data("input")
part_two()
part_one()
test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()mul(12,12)"
test = re.sub(r"don't\(\).+do\(\)", "", test)
test = re.sub(r"don't\(\).+", "", test,1)
print(test)
