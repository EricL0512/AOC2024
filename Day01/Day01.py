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
    for index, i in enumerate(sorted(left)):
        result += abs(sorted(left)[index] - sorted(right)[index])
    print(f"part one: {result}")


def part_two():
    result = 0
    left = []
    right = []
    for i in file_data:
        left.append(int(i.split(" ")[0]))
        right.append(int(i.split(" ")[-1]))
    for i in left:
        result += i * right.count(i)
    print(f"part two: {result}")


file_data = get_file_data("input")
part_one()
part_two()
