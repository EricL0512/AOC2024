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
    total = 0
    for line in file_data:
        while line.find("don't()") != -1:
            start_remove = line.find("don't()")
            end_remove = line.find("do()")
            print(f"{start_remove} {end_remove}")
            if start_remove == -1 and end_remove == -1:
                break
            elif line.find("do()") == -1 and line.find("don't()") != -1:
                line = line[:start_remove]
                continue
            else:
                if start_remove < end_remove:
                    line = line[0:start_remove] + line[end_remove + 4:]
                    print("s")
                else:
                    break

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
    print("skibigi")


file_data = get_file_data("input")
test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
s = test_str.find("don't()")
e = test_str.find("do()")

test_str1 = test_str[0:s] + test_str[e + 4:]
print(test_str1)
part_two()
