def tribonacci(n):
    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    first, second = 0, 1
    third = first + second
    for _ in range(2, n):
        result = first + second + third
        first, second, third = second, third, result

    return third


res = tribonacci(25)
print(res)
