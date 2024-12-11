from typing import TextIO


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def part_one():
    stones = file_data[0].split(" ")
    test = stones.copy()
    for c, char in enumerate(test):
        if int(char) == 0:
            stones[c] = 1
        elif len(char) % 2 == 0:
            print(stones)
            stones.pop(c)
            stones.append(char[len(char)//2:])
            stones.append(char[:len(char)//2])
            print(stones)
        else:
            stones.append(str(int(stones.pop(c)) * 2024))

def part_two():
    pass


file_data = get_file_data("input")
part_one()
