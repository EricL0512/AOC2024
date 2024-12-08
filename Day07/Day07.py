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
        target, *equation = (int(item) for item in (line.replace(":", " ").split()))
        """
        short version: binary tree
        
        All the possible combinations of operations for an equation (NOTE: that there is one less operation than term)
        Ex: 1 + 2 has two terms but only one operation operations = terms-1
        """
        operator_perm = list(itertools.product("*+", repeat=len(equation) - 1))
        # Converts each equation element into a integer
        for operation in operator_perm:
            tmp = equation[0]
            """
            Modified version of partial sums. Instead of tmp being the sum of each of the previous elements, tmp can be 
            multiplicative or additive? (as in combining the digits of two numbers)
            """
            for n in range(len(equation[:-1])):
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
        target, *equation = (int(item) for item in (line.replace(":", " ").split()))
        """
        short version: binary tree
        
        All the possible combinations of operations for an equation (NOTE: that there is one less operation than term)
        Ex: 1 + 2 has two terms but only one operation operations = terms-1
        """
        operator_perm = list(itertools.product("*+|", repeat=len(equation) - 1))
        # Converts each equation element into a integer
        for operation in operator_perm:
            tmp = equation[0]
            """
            Modified version of partial sums. Instead of tmp being the sum of each of the previous elements, tmp can be 
            multiplicative or additive? (as in combining the digits of two numbers)
            """
            for n in range(len(equation[:-1])):
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

r"""
Binary Tree Visualization (only + and *, 2 terms total)

                        None 
                       /    \ 
                     +        *                                                 
                    / \      / \  
                   /   \    /   \ 
                  ++   +*  *+    +*                   
        
result: (++, +*, *+, +*)                                                                                                        
"""
