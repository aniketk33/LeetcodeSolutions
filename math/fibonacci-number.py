def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(3, n + 1):
        curr_sum = prev + curr
        prev = curr
        curr = curr_sum

    return prev + curr


res = fib(100)
print(res)
