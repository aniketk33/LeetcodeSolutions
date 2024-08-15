"""refer FREEFORM for better understanding"""
from typing import List
from collections import defaultdict


def valid_sudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    grids = defaultdict(set)

    for curr_row in range(9):
        for curr_column in range(9):
            if board[curr_row][curr_column] == '.':
                continue

            curr_val = board[curr_row][curr_column]
            # check for three conditions.
            # 1. if it is present in the entire row or column or the current grids
            if (curr_val in rows[curr_row] or curr_val in columns[curr_column] or
                    curr_val in grids[(curr_row // 3, curr_column // 3)]):
                return False

            # add the curr number in row, column and the grids
            rows[curr_row].add(curr_val)
            columns[curr_column].add(curr_val)
            grids[(curr_row // 3, curr_column // 3)].add(curr_val)

    return True


input_board = [[".", "8", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", "2", ".", ".", ".", "."],
               [".", "6", ".", ".", ".", ".", "1", ".", "4"], [".", ".", ".", "9", ".", ".", "7", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", "4", "."], [".", ".", "1", ".", ".", "8", ".", ".", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "5", ".", "7", "."],
               [".", ".", "3", ".", ".", "5", "6", ".", "."]]
res = valid_sudoku(input_board)
print(res)
