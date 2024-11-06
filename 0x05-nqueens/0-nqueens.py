#!/usr/bin/python3
"""
Modue for the nqueens problem
"""

import sys


# Creating an attack checkers, they receive an arrat containing
# the coordination for each piece, List[Tuple]

# make these functions return False if there's an attacking queen
# Returns true in not attacking


queens = {}

def diag_safe(queen_dict, curr_key):
    """Check if all pieces are safe diagnally
    """
    # Check if there's an attack from any queen to any queen:
    for key, value in queen_dict.items():
        if key != curr_key and curr_key < int(sys.argv[1]):
            x_diff = abs(queen_dict[curr_key][0] - queen_dict[key][0])
            y_diff = abs(queen_dict[curr_key][1] - queen_dict[key][1])
            if x_diff == y_diff:
                if queen_dict[curr_key][0] < int(sys.argv[1]):
                    queen_dict[curr_key][0] += 1
                    return False
            elif queen_dict[curr_key][1] < int(sys.argv[1]):
                    queen_dict[curr_key][1] += 1
                    return False
            else:
                return False
    return True



def row_safe(queen_dict, curr_key):
    # wont work!
    if queen_dict[curr_key][0] == queen_dict[key][0]:
        queen_dict[curr_key][1] += 1
        return False
    if queen_dict[curr_key][1] == queen_dict[curr_key][1] % int(sys.argv[1]): 
        return False
    return col_safe(queen_dict, key, int(sys.argv[1]) + 1)


def col_safe(queen_dict, key):
    # wont work!
    if queen_dict[curr_key][1] == queen_dict[key][1]:
        queen_dict[curr_key][0] += 1
        return True
    if queen_dict[curr_key][0] == queen_dict[curr_key][0] % int(sys.argv[1]): 
        return False
    return col_safe(queen_dict, key, int(sys.argv[1]) + 1)


def recursive_method(key):
    # Can work!
    if diag_safe(queens, key) and row_safe(queens, key) and col_safe(queens, key) and key < 4:
        result = [value for _, value in queens.items()]
        print(result)
    if (key + 1) < 4:
        return recursive_method(key + 1)


def nqueens():
    """How many ways are possible to place N queens such that
    No queen is attacking another?

    We will get all the solutions, count them and print them
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = sys.argv[1]
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for i in range(int(sys.argv[1])):
        queens[i] = [i,i]

    recursive_method(0)

if __name__ == "__main__":
    nqueens()
