"""refer FREEFORM for better understanding and leetcode 79 question"""
from typing import List


def word_search(board: List[List[str]], word: str):
    # get the total rows and columns of the board
    ROWS, COLUMNS = len(board), len(board[0])
    visited_path = set()

    def dfs(curr_row, curr_column, word_idx):
        # check if it is the last index of the word
        if word_idx == len(word):
            return True

        # check for out of boundary conditions.
        # 1. less than zero is checked because we are checking for adjacent values too.
        # 2. if current row and column are not in the visited path set
        # 3. if word is not on the board
        if (curr_row >= ROWS or curr_column >= COLUMNS or
                curr_row < 0 or curr_column < 0 or
                (curr_row, curr_column) in visited_path or
                word[word_idx] != board[curr_row][curr_column]):
            return False

        # after all the checks are satisfied, add the current row and column
        visited_path.add((curr_row, curr_column))
        # send all the adjacent locations
        result = (dfs(curr_row + 1, curr_column, word_idx + 1) or
                  dfs(curr_row - 1, curr_column, word_idx + 1) or
                  dfs(curr_row, curr_column + 1, word_idx + 1) or
                  dfs(curr_row, curr_column - 1, word_idx + 1))
        # remove the path after visiting
        visited_path.remove((curr_row, curr_column))

        return result

    # iterate over the board
    for row in range(ROWS):
        for column in range(COLUMNS):
            if dfs(row, column, 0):
                return True

    return False
