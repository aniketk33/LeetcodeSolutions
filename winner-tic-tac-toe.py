def winner(moves):
    # create rows, cols and two diagonal variables of size n
    n = 3
    rows = [0] * n
    cols = [0] * n
    d1 = d2 = 0

    # increment value for player A and decrement for player B in every variable
    for i, (row, col) in enumerate(moves):
        player = 'A' if i % 2 == 0 else 'B'
        sign = 1 if player == 'A' else -1
        rows[row] += sign
        cols[col] += sign

        # for left-to-right diagonal
        if row == col:
            d1 += sign
        # for right-to-left diagonal
        if row + col == n - 1:
            d2 += sign

        # check for winner, i.e., who reaches n first
        if abs(rows[row]) == n or abs(cols[col]) == n or abs(d1) == n or abs(d2) == n:
            return player

    # if all the grids are not filled, then the game is still pending
    return 'Draw' if len(moves) == (n * n) else 'Pending'


res = winner([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
print(res)
