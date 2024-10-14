def power_three(n):
    if n <= 0:
        return False
    count = 0
    result = n

    while n > 1:
        n = n / 3
        count += 1

    return 3 ** count == result


def power_three_2(n):
    while n >= 3:
        n = n / 3
    return n == 1


def power_three_3(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n = n / 3

    return n == 1


# res = power_three(45)
# res = power_three_2(45)
res = power_three_3(45)
print(res)
