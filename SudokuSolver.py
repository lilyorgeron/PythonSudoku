import numpy as np

"""
Functions needed:

Driver code

Recursive to fill out board

Checking relevant rows, columns, and 3x3 for any repeats of #s 1-9

"""


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


def create_dicts(dim, board):
    # creating hash maps
    row_map = {}
    col_map = {}
    grid_map = {}
    for i in range(dim):
        # row dicts
        row = {}
        for item in board[i]:
            if item > 0:
                if (item in row):
                    row[item] += 1
                else:
                    row[item] = 1
        row_map[str(i)] = row
        # column dicts
        column = {}
        for item in board[:,i]:
            if item > 0:
                if (item in column):
                    column[item] += 1
                else:
                    column[item] = 1
        col_map[str(i)] = column
        # grid dicts
        grid = {}
        # using arithmetic to create bounds on grids
        # (come back later and take out hard-coded 3)
        xbound = (3*i) % dim
        ybound = (i // 3) * 3
        for x in range(xbound, xbound + 3):
            for y in range(ybound, ybound + 3):
                item = board[y][x]
                if item > 0:
                    if (item in grid):
                        grid[item] += 1
                    else:
                        grid[item] = 1
        grid_map[str(i)] = grid
        print(grid_map[str(i)])

    return

create_dicts(dim, board)


# def check_if_break(num, i):

#     # using a dictionary to check for number frequencies
#     repeats = {}
#     # checking each column in row
#     for j in range(dim):
#         square = board[i][j]
#         if square >= 1 and square <= 9:
#             if square in repeats:
#                 repeats[square] += 1
#             else:
#                 repeats[square] = 1



    
#     return





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