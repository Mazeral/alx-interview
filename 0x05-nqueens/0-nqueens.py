#!/usr/bin/python3
"""
Modue for the nqueens problem
"""

import sys


# Creating an attack checkers, they receive an arrat containing
# the coordination for each piece, List[Tuple]

# make these functions return False if there's an attacking queen
# Returns true in not attacking
def diag_safe(queen_dict, curr_key, n):
    """Check if all pieces are safe diagnally
    """
    # Check if there's an attack from any queen to any queen:
    for key, value in queen_dict:
        if key != curr_key:
            x_diff = abs(queen_dict[curr_key][0] - queen_dict[key][0])
            y_diff = abs(queen_dict[curr_key][1] - queen_dict[key][1])
            if x_diff == y_diff:
                if queen_dict[curr_key][0] < n + 1:
                    queen_dict[curr_key][0] += 1
                    return False
            elif queen_dict[curr_key][1] < n + 1:
                    queen_dict[curr_key][1] += 1
                    return False
            else:
                return False
    return True



def row_safe(queen_dict, curr_key, n):
    for key, value in queen_dict:
        if queen_dict[curr_key][0] == queen_dict[key][0]:
            # Move one of them
            if queen_dict[curr_key][0] < n + 1:
                queen_dict[curr_key][0] += 1
                return False
            elif queen_dict[key][0] < n + 1:
                queen_dict[key][0] += 1
            else:
                return False
    return True


def col_safe(queen_dict, key, n):
    for key, value in queen_dict:
        if queen_dict[curr_key][1] == queen_dict[key][1]:
            # Move one of them
            if queen_dict[curr_key][1] < n + 1:
                queen_dict[curr_key][1] += 1
                return False
            elif queen_dict[key][1] < n + 1:
                queen_dict[key][1] += 1
            else:
                return False
    return True


def get_last_key(queens):
    last_key
    for key in queens:
        last_key = key
    return last_key

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

    queens = {}
    solutions = []
    for i in range(1, n + 1):
        queens[i] = [i,i]

    for dic_key, dic_value in queens:
        for queen_key, queen_value in queens:
            if col_attack(queens, queen_key, n) and
            row_attack(queens, queen_key, n) and
            diag_attack(queens, queen_key, n):
                solution = [value for key, value in queens]
                solutions.append(solution)


if __name__ == "__main__":
    nqueens()
