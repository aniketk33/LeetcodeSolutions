def guess_number(n):
    left_ptr, right_ptr = 1, n

    while True:
        mid = left_ptr + (right_ptr - left_ptr) // 2
        # uncomment this line as the function is implemented in the leetcode description
        # curr_guess = guess(mid)
        curr_guess = 0
        if curr_guess < 0:
            right_ptr = mid - 1
        elif curr_guess > 0:
            left_ptr = mid + 1
        else:
            return mid
