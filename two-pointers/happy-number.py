def happy(n):
    def find_squares(num):
        square = 0
        while num > 0:
            remainder = num % 10
            square += remainder ** 2
            num = num // 10

        return square

    # takes one step
    slow_pointer = find_squares(n)
    # always two-step ahead
    fast_pointer = find_squares(find_squares(n))

    while slow_pointer != fast_pointer and fast_pointer != 1:
        slow_pointer = find_squares(slow_pointer)
        fast_pointer = find_squares(find_squares(fast_pointer))

    return fast_pointer == 1


res = happy(19)
print(res)
