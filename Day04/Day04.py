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
    two_de: list[list[str]] = []
    column_major: list[list[str]] = []
    for line in file_data:
        temp_list = []
        for s in line:
            temp_list.append(s)
        two_de.append(temp_list)

    #  pad the 2d list

    for i in range(len(two_de)):
        temp_list = []
        for j in two_de[i]:
            temp_list.append(".")
        two_de.append(temp_list)
        two_de.insert()




def part_two():
    pass


file_data = get_file_data("input")
part_one()
