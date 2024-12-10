from typing import TextIO

def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def find_paths(curr_number, row, column, total):
    if curr_number == 9:
        return total
    try:
        if file_data2[row+1][column] == curr_number + 1:
            total += find_paths(curr_number+1, row+1, column, total)
    except IndexError:
        pass
    try:
        if file_data2[row-1][column] == curr_number + 1:
            total += find_paths(curr_number+1, row-1, column, total)
    except IndexError:
        pass
    try:
        if file_data2[row][column+1] == curr_number + 1:
            total += find_paths(curr_number+1, row, column+1, total)
    except IndexError:
        pass
    try:
        if file_data2[row][column-1] == curr_number + 1:
            total += find_paths(curr_number+1, row, column-1, total)
    except IndexError:
        return total
    return total
def part_one():
    total = 0
    for r, row in enumerate(file_data2):
        for c, column in enumerate(row):
            if column == 0:
                print(r, c)
                total = find_paths(column, r, c, 0)
    print(total)


def part_two():
    pass


file_data = get_file_data("input")
file_data2 = []
total = 0
for i in file_data:
    temp = []
    for j in i:
        temp.append(int(j))
    file_data2.append(temp)
part_one()
