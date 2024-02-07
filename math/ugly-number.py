def ugly_num(n):
    prime = [2, 3, 5]
    for p in prime:
        while n % p == 0 and n > 0:
            n = n // p

    return n == 1


res = ugly_num(20)
print(res)
