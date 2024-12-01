from typing import TextIO


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def part_one():
    result = 0
    left = []
    right = []
    for i in file_data:
        left.append(int(i.split(" ")[0]))
        right.append(int(i.split(" ")[-1]))
        left.sort()
        right.sort()
    for index in range(len(left)):
        result += abs(left[index] - right[index])
    print(f"part one: {result}")




def part_two():
    result = 0
    left = []
    right = []
    for i in file_data:
        left.append(int(i.split(" ")[0]))
        right.append(int(i.split(" ")[-1]))
    for i in left:
        count = 0
        for j in right:
            if i == j:
                count += 1
        result += i * count
    print(f"part two: {result}")


file_data = get_file_data("input")
part_one()
part_two()
