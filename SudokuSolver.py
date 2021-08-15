import numpy as np

"""
Functions needed:

Driver code

Recursive to fill out board

Checking relevant rows, columns, and 3x3 for any repeats of #s 1-9

"""

# board and hash-map set-up
board = np.array([[0, 0, 6, 0, 5, 4, 9, 0, 0],
                  [1, 0, 0, 0, 6, 0, 0, 4, 2],
                  [7, 0, 0, 0, 8, 9, 0, 0, 0],
                  [0, 7, 0, 0, 0, 5, 0, 8, 1],
                  [0, 5, 0, 3, 4, 0, 6, 0, 0],
                  [4, 0, 2, 0, 0, 0, 0, 0, 0],
                  [0, 3, 4, 0, 0, 0, 1, 0, 0],
                  [9, 0, 0, 8, 0, 0, 0, 5, 0],
                  [0, 0, 0, 4, 0, 0, 3, 0, 7]])

dim = len(board[0])

row_map = {}
col_map = {}
grid_map = {}

found = False

##############################

def create_dicts(dim, board):
    # creating hash maps
    for a in range(dim):
        # row dicts
        row = {}
        for item in board[a]:
            if item > 0:
                if (item in row):
                    row[item] += 1
                else:
                    row[item] = 1
        row_map[a] = row
        # column dicts
        column = {}
        for item in board[:,a]:
            if item > 0:
                if (item in column):
                    column[item] += 1
                else:
                    column[item] = 1
        col_map[a] = column
        # grid dicts
        grid = {}
        # using arithmetic to create bounds on grids
        # (come back later and take out hard-coded 3)
        xbound = (3*a) % dim
        ybound = (a // 3) * 3
        for x in range(xbound, xbound + 3):
            for y in range(ybound, ybound + 3):
                item = board[y][x]
                if item > 0:
                    if (item in grid):
                        grid[item] += 1
                    else:
                        grid[item] = 1
        grid_map[a] = grid

    return



def check_if_break(num, i, j):

    # checking row dict
    print(row_map[i], num, i, j)
    print(type(row_map[i]))
    if num in row_map[i]:
        return True

    # checking column dict
    if num in col_map[j]:
        return True

    # checking grid dict
    grid = (j//3) + 3*(i//3)
    if num in grid_map[grid]:
        return True

    # no breaks
    return False


def solver(row, col):

    # base case (completed final row)
    if row == dim:
        global found
        found = True
        return

    # if space contains predetermined number
    if board[row][col]:
        # call function for next square
        # if at end of the row
        if (col+1) == dim:
            solver(row+1, 0)
        # continue in same row
        else:
            solver(row, col+1)
            
    else:
        for num in range(1, dim+1):
            if not check_if_break(num, row, col):
                board[row][col] = num

                # adjusting dictionaries
                row_map[row][num] = 1
                col_map[col][num] = 1

                grid = (col//3) + 3*(row//3)
                grid_map[grid][num] = 1

                # if at end of the row
                if (col+1) == dim:
                    solver(row+1, 0)
                # continue in same row
                else:
                    solver(row, col+1)

                if found:
                    return True

                # return to blank
                board[row][col] = 0
                del row_map[row][num]
                del col_map[col][num]
                del grid_map[grid][num]


    return False


##############################


# setting up dictionaries for board
create_dicts(dim, board)

if solver(0,0):
    solution = board
    for row in solution:
        print(row)
else:
    print("No solution found!")

""" 
Solution:

board = [[2, 8, 6, 1, 5, 4, 9, 7, 3],
         [1, 9, 5, 7, 6, 3, 8, 4, 2],
         [7, 4, 3, 2, 8, 9, 5, 1, 6],
         [3, 7, 9, 6, 2, 5, 4, 8, 1],
         [8, 5, 1, 3, 4, 7, 6, 2, 9],
         [4, 6, 2, 9, 1, 8, 7, 3, 5],
         [6, 3, 4, 5, 7, 2, 1, 9, 8],
         [9, 1, 7, 8, 3, 6, 2, 5, 4],
         [5, 2, 8, 4, 9, 1, 3, 6, 7]]

"""




