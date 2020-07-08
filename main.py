# project goal: to write a module to solve sudoku puzzles using Recursive Backtracking

# please note that this code will provide the first satisfying solution
# hence, this code cannot be used to answer the question whether the solution is unique


def empty_cell(su):
    """Finds a 0 entry and returns its location as a tuple."""
    for i in range(0, len(su)):
        for j in range(0, len(su)):
            if su[i][j] == 0:
                return i, j
    return None


def validate(su, loc, num):
    """
    This function validates that the chosen integer staisfies all of the sudoku rules.
    There can only be one of each numbers from 1 to 9 in every row, column and 3x3 square.
    It will return True if the selected number satisfies all the conditions and False if
    at least one of them is not satisfied.

    :param list su: list of lists, that represents the sudoku board
    :param tuple loc: row and column of the empty cell
    :param int num: the number from 1 to 9 we are validating
    :return: True if satisfies all conditions, False if not
    """

    row = loc[0]
    col = loc[1]

    # check the row
    for r in su[row]:
        if r == num:  # do we need to mention to avoid itself?
            return False

    # check the column
    for rw in su:
        if rw[col] == num:
            return False

    # check the 3x3 square
    sqr_x = range(row // 3 * 3, row // 3 * 3 + 3)
    sqr_y = range(col // 3 * 3, col // 3 * 3 + 3)

    for x in sqr_x:
        for y in sqr_y:
            if su[x][y] == num:
                return False

    return True


def solve(su):
    """
    The main function that solves the sudoku puzzle using recursive backtracking.
    This function also calls empty_cell and validate functions.
    :param list su: list of lists, consisting of integers
    :return: True if solution exists, False if it does not
    """

    loc = empty_cell(su)
    if loc is None:
        return True  # mb change it to message later

    for num in range(1, 10):
        if validate(su, loc, num):  # validate needs to return True to make this work
            su[loc[0]][loc[1]] = num

            if solve(su):
                return True

            su[loc[0]][loc[1]] = 0

    return False  # change it to message


def print_solved(su):
    """
    This function prints the finals solved version of the input sudoku puzzle.
    :param list su: the solved sudoku in the form of list of lists
    :return: None
    """

    if solve(su):
        for line in su:
            print(line)


puzzle_1 = [
    [7, 8, 5, 4, 3, 9, 1, 2, 6],
    [6, 1, 2, 8, 7, 5, 3, 4, 9],
    [0, 9, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

puzzle_2 = [
    [9, 1, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 9, 0],
    [0, 0, 2, 0, 9, 0, 4, 0, 0],
    [0, 7, 9, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 5, 8],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 5, 0, 3, 0, 4]
]

print_solved(puzzle_2)