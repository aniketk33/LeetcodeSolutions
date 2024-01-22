def solve(board):
    # create the rows, columns, and the boxes of the sudoku board
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            curr_num = int(board[r][c])
            rows[r].add(curr_num)
            columns[c].add(curr_num)

            box_id = r // 3 * 3 + c // 3
            boxes[box_id].add(curr_num)

    solved = False

    def backtrack(curr_r, curr_j):
        nonlocal solved
        if curr_r == 9:
            solved = True
            return

        new_r = curr_r + (curr_j + 1) // 9
        new_c = (curr_j + 1) % 9

        # skip if the current coordinates are non-empty by moving to new coordinates
        if board[curr_r][curr_j] != '.':
            backtrack(new_r, new_c)
        else:
            for num in range(1, 10):
                curr_box_id = curr_r // 3 * 3 + curr_j // 3
                if num in rows[curr_r] or num in columns[curr_j] or num in boxes[curr_box_id]:
                    continue

                # add the current number to rows, columns, boxes, and update the board
                rows[curr_r].add(num)
                columns[curr_j].add(num)
                boxes[curr_box_id].add(num)
                board[curr_r][curr_j] = str(num)

                backtrack(new_r, new_c)

                if not solved:
                    rows[curr_r].remove(num)
                    columns[curr_j].remove(num)
                    boxes[curr_box_id].remove(num)
                    board[curr_r][curr_j] = '.'

    backtrack(0, 0)


input_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solve(input_board)
print(input_board)
