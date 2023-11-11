"""refer FREEFORM for better understanding"""
from typing import List
from collections import defaultdict


def valid_sudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    grid = defaultdict(set)

    for curr_row in range(9):
        for curr_column in range(9):
            if board[curr_row][curr_column] == '.':
                continue

            # check for three conditions.
            # 1. if it is present in the entire row or column or the current grid
            if (board[curr_row][curr_column] in rows[curr_row] or
                    board[curr_row][curr_column] in columns[curr_column] or
                    board[curr_row][curr_column] in grid[(curr_row // 3, curr_column // 3)]):
                return False

            # add the curr number in row, column and the grid
            rows[curr_row].add(board[curr_row][curr_column])
            columns[curr_column].add(board[curr_row][curr_column])
            grid[(curr_row // 3, curr_column // 3)].add(board[curr_row][curr_column])

    return True
