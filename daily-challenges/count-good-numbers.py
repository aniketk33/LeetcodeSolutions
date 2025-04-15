# need a re-visit
def count_numbers(n):
    primes = [2, 3, 5, 7]
    evens = [i for i in range(0, 9, 2)]
    result = 0
    start = 0 if n == 1 else 10 ** (n - 1)
    end = 10 ** n

    for i in range(start, end):
        is_even = is_prime = True
        for idx, digit in enumerate(str(i)):
            if idx % 2 == 0 and int(digit) not in evens:
                is_even = False
                break
            if idx % 2 != 0 and int(digit) not in primes:
                is_prime = False
                break
        if is_even and is_prime:
            result += 1

    return result % (10 ** 9 + 7)


def count_numbers_2(n):
    mod = 10 ** 9 + 7
    # even indices
    evens = (n + 1) // 2
    odds = n // 2

    # there are only 5 even digits (0,2,4,6,8) and 4 prime digits (2,3,5,7), hence the below equation
    return pow(5, evens, mod) * pow(4, odds, mod) % mod


# res = count_numbers(4)
res = count_numbers_2(50)
print(res)
