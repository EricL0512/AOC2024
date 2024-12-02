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
        is_safe = True
        levels = line.split(" ")

        if not (sorted(levels, key=int) == levels or list(reversed(levels)) == sorted(levels, key=int)):
            is_safe = False
        for index in range(len(levels) - 1):
            if abs(int(levels[index]) - int(levels[index+1])) > 3 or int(levels[index]) == int(levels[index + 1]):
                is_safe = False
                break
        if is_safe:
            total += 1
        else:
            pass
    print(f"part one: {total}")




def part_two():
    total = 0
    for line in file_data:
        is_safe = True
        levels = line.split(" ")
        temp_levels = list(levels)
        for i in range(len(levels)):
            is_safe = True
            levels = list(temp_levels)
            if not i == range(len(levels)):  # tests to see what would occur if nothing is removed
                levels.pop(i)
            if not (sorted(levels, key=int) == levels or list(reversed(levels)) == sorted(levels, key=int)):
                is_safe = False
            for index in range(len(levels) - 1):
                if abs(int(levels[index]) - int(levels[index + 1])) > 3 or int(levels[index]) == int(levels[index + 1]):
                    is_safe = False
                    break
            if is_safe:
                total += 1
                break
            else:
                continue
    print(f"part two: {total}")


file_data = get_file_data("input")
part_one()
part_two()
