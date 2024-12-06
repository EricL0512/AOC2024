import cProfile
from typing import TextIO


def get_file_data(file_name) -> list[str]:
    f: TextIO = open(file_name)
    data: list[str] = []
    for line in f:
        data.append(line.rstrip())
    return data


def part_one():
    pos = [0, 0]
    directions = {"^": ">", ">": "v", "v": "<", "<": "^"}
    two_di = []
    two_di += (list(i) for i in file_data)
    curr_direction = "^"
    found_start = False
    for r, row in enumerate(two_di):
        if found_start:
            break
        for c, char in enumerate(row):
            if found_start:
                break
            if char == "^":
                pos = [r, c]
                found_start = True
    pos_start = list(pos)
    count = 1  # First position already covered
    past_pos = [[pos[0], pos[1]]]  # Just in case the guard passes the same points, first position already covered
    while True:
        try:
            if not (pos[0] > 0 and pos[1] > 0):
                break
            if curr_direction == "^":
                if two_di[pos[0] - 1][pos[1]] != "#":
                    pos[0] -= 1
                    if not [pos[0], pos[1]] in past_pos:
                        count += 1
                    past_pos.append([pos[0], pos[1]])
                else:
                    curr_direction = directions[curr_direction]
            elif curr_direction == ">":
                if two_di[pos[0]][pos[1] + 1] != "#":
                    pos[1] += 1
                    if not [pos[0], pos[1]] in past_pos:
                        count += 1
                    past_pos.append([pos[0], pos[1]])
                else:
                    curr_direction = directions[curr_direction]
            elif curr_direction == "v":
                if two_di[pos[0]+1][pos[1]] != "#":
                    pos[0] += 1
                    if not [pos[0], pos[1]] in past_pos:
                        count += 1
                    past_pos.append([pos[0], pos[1]])
                else:
                    curr_direction = directions[curr_direction]
            elif curr_direction == "<":
                if two_di[pos[0]][pos[1] - 1] != "#":
                    pos[1] -= 1
                    if not [pos[0], pos[1]] in past_pos:
                        count += 1
                    past_pos.append([pos[0], pos[1]])
                else:
                    curr_direction = directions[curr_direction]
        except IndexError:
            break
    print(f"part one: {count}")
    return past_pos, pos_start


# Brute force probably because not time limited
# Will pass past_pos from part_one into part_two for simplicity
# ~ symbol will be used to represent path

"""
How this works: 
    track out the path that the guard takes, replacing each . with a ~ (lets call this the formatted list)
    
    take the formatted list replace the first ~ with a # and test for repetition
        - traverse this list using the rules given (turn when you hit a #, continue otherwise)
        -repetition is tracked using a list of tuples, with each tuple containing 3 elements:
            1. y position
            2. x position
            3. orientation (^, >, v, <)
        if you touch a # and the point and orientation match a tuple in the list, you are in a loop (continue on)
    then, check again, but instead of replacing the first ~, you replace the second ~. Continue till all combinations
    are exhausted
    
    add all instances where you are in a loop: that is your final answer
"""


def part_two(past_pos, pos):
    two_di = []
    two_di += (list(i) for i in file_data)
    for pair in past_pos:
        two_di[pair[0]][pair[1]] = "~"

    # Make a list to keep track of times you hit a #
    count = 0
    directions = {"^": ">", ">": "v", "v": "<", "<": "^"}
    curr_direction = "^"
    start_pos = list(pos)
    for r, row in enumerate(two_di):
        for c, char in enumerate(row):

            if char != "~":
                continue
            two_di[r][c] = "#"
            pos = list(start_pos)
            curr_direction = "^"
            hash_touched = set()

            while True:
                try:
                    if not (pos[0] > 0 and pos[1] > 0):
                        break
                    if curr_direction == "^":
                        if two_di[pos[0] - 1][pos[1]] != "#":
                            pos[0] -= 1
                        else:
                            if (pos[0], pos[1], "^") in hash_touched:
                                count += 1
                                break
                            hash_touched.add((pos[0], pos[1], "^"))
                            curr_direction = directions[curr_direction]
                    elif curr_direction == ">":
                        if two_di[pos[0]][pos[1] + 1] != "#":
                            pos[1] += 1
                        else:
                            if (pos[0], pos[1], ">") in hash_touched:
                                count += 1
                                break
                            hash_touched.add((pos[0], pos[1], ">"))
                            curr_direction = directions[curr_direction]
                    elif curr_direction == "v":
                        if two_di[pos[0] + 1][pos[1]] != "#":
                            pos[0] += 1
                        else:
                            if (pos[0], pos[1], "v") in hash_touched:
                                count += 1
                                break
                            hash_touched.add((pos[0], pos[1], "v"))
                            curr_direction = directions[curr_direction]
                    elif curr_direction == "<":
                        if two_di[pos[0]][pos[1] - 1] != "#":
                            pos[1] -= 1
                        else:
                            if (pos[0], pos[1], "<") in hash_touched:
                                count += 1
                                break
                            hash_touched.add((pos[0], pos[1], "<"))
                            curr_direction = directions[curr_direction]
                except IndexError:
                    break
            two_di[r][c] = "~"
    print(f"part two: {count}")


file_data = get_file_data("input")
past_pos, pos = part_one()
part_two(past_pos, pos)
