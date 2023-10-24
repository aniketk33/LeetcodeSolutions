"""refer FREEFORM for better understanding"""


def n_queens(n):
    result = []
    used_column = set()
    positive_diagonal = set()
    negative_diagonal = set()
    board = [['.'] * n for _ in range(n)]

    def backtrack(curr_row):
        if curr_row == n:
            path = [''.join(row) for row in board]
            result.append(path)
            return

        for curr_column in range(n):
            if (curr_column in used_column or (curr_row - curr_column) in negative_diagonal or
                    (curr_row + curr_column) in positive_diagonal):
                continue

            board[curr_row][curr_column] = 'Q'
            # add all the position of the queen can move to the used set
            used_column.add(curr_column)
            positive_diagonal.add(curr_row + curr_column)
            negative_diagonal.add(curr_row - curr_column)

            # recursive call to the next row
            backtrack(curr_row + 1)

            board[curr_row][curr_column] = '.'
            # reset all the positions
            used_column.remove(curr_column)
            positive_diagonal.remove(curr_row + curr_column)
            negative_diagonal.remove(curr_row - curr_column)

    backtrack(0)
    return result


res = n_queens(4)
print(res)
