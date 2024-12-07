from typing import TextIO
import itertools


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def part_one():
    count = 0
    for line in file_data:
        target = int(line.split(":")[0])
        equation = line.split(":")[1][1:]
        equation = equation.split(" ")
        operator_perm = list(itertools.product("*+", repeat=len(equation) - 1))
        equation2 = list(int(i) for i in equation)
        equation = equation2
        for operation in operator_perm:
            tmp = equation[0]
            for n, num in enumerate(equation[:-1]):
                if operation[n] == "*":
                    tmp = (tmp * equation[n + 1])
                if operation[n] == "+":
                    tmp = (tmp + equation[n + 1])
            if target == tmp:
                count += target
                break
    print(f"part one: {count}")


def part_two():
    count = 0
    for line in file_data:
        target = int(line.split(":")[0])
        equation = line.split(":")[1][1:]
        equation = equation.split(" ")
        operator_perm = list(itertools.product("*+|", repeat=len(equation) - 1))
        equation2 = list(int(i) for i in equation)
        equation = equation2
        for operation in operator_perm:
            tmp = equation[0]
            for n, num in enumerate(equation[:-1]):
                if operation[n] == "*":
                    tmp = (tmp * equation[n + 1])
                if operation[n] == "+":
                    tmp = (tmp + equation[n + 1])
                if operation[n] == "|":
                    tmp = int(str(tmp) + str(equation[n + 1]))
            if target == tmp:
                count += target
                break
    print(f"part two: {count}")


file_data = get_file_data("input")
part_one()
part_two()
