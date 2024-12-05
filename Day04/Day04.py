from typing import TextIO


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def part_one():
    #  make 2D List, pad list perimeter
    total = 0
    padded_list: list[list[str]] = []
    temp_list = []
    #  pad left and right
    for line in file_data:
        temp_list = ["~", "~", "~"]
        for char in line:
            temp_list.append(char)

        for repeat in range(3):
            temp_list.append("~")

        padded_list.append(temp_list)
    # pad top and bottom
    temp_list2 = []
    for i in temp_list:

        temp_list2.append("~")

    for repeat in range(3):
        padded_list.append(temp_list2)
        padded_list.insert(0, temp_list2)
    # list is now fully padded, check for instances of XMAS
    for y, line in enumerate(padded_list):
        for x, char in enumerate(line):
            if char != "X":
                continue
            #  W to E horizontal
            if line[x + 1:x + 4] == ["M", "A", "S"]:
                total += 1
            # E to W horizontal
            if line[x - 3:x] == ["S", "A", "M"]:
                total += 1
            # N to S vertical
            if padded_list[y+1][x] + padded_list[y+2][x] + padded_list[y+3][x] == "MAS":
                total += 1
            # S to N vertical
            if padded_list[y - 1][x] + padded_list[y - 2][x] + padded_list[y - 3][x] == "MAS":
                total += 1
            # NW to SE diagonal
            if padded_list[y - 1][x - 1] + padded_list[y - 2][x - 2] + padded_list[y - 3][x - 3] == "MAS":
                total += 1
            if padded_list[y + 1][x + 1] + padded_list[y + 2][x + 2] + padded_list[y + 3][x + 3] == "MAS":
                total += 1
            # NE to SW diagonal
            if padded_list[y + 1][x - 1] + padded_list[y + 2][x - 2] + padded_list[y + 3][x - 3] == "MAS":
                total += 1
            if padded_list[y - 1][x + 1] + padded_list[y - 2][x + 2] + padded_list[y - 3][x + 3] == "MAS":
                total += 1
    print(f"part 1: {total}")


def part_two():
    total = 0
    padded_list: list[list[str]] = []
    temp_list = []
    for line in file_data:
        temp_list = ["~", "~", "~"]
        for char in line:
            temp_list.append(char)

        for repeat in range(3):
            temp_list.append("~")

        padded_list.append(temp_list)
    temp_list2 = []
    for i in temp_list:
        temp_list2.append("~")

    for repeat in range(3):
        padded_list.append(temp_list2)
        padded_list.insert(0, temp_list2)
    # Code changes starting here

    for y, line in enumerate(padded_list):
        for x, char in enumerate(line):
            if char != "A":
                continue
            # Brute force every possible combination (4 total combinations)
            # Since making a cross requires 2 MAXs
            # NW to SE diagonal
            amount_of_max = 0
            if padded_list[y-1][x-1] + padded_list[y+1][x+1] == "MS":
                amount_of_max += 1
            # SE to VW diagonal (NW to SE diagonal reversed)
            if padded_list[y - 1][x - 1] + padded_list[y + 1][x + 1] == "SM":
                amount_of_max += 1
            # NE to SW diagonal
            if padded_list[y-1][x+1] + padded_list[y+1][x-1] == "MS":
                amount_of_max += 1
            # SW to NE diagonal (NE to SW diagonal reversed)
            if padded_list[y - 1][x + 1] + padded_list[y + 1][x - 1] == "SM":
                amount_of_max += 1
            if amount_of_max >= 2:
                total += 1
    print(f"part 2: {total}")


file_data = get_file_data("input")
part_one()
part_two()
