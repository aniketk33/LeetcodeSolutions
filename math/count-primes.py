def count_primes(n):
    count = 0

    for i in range(2, n):
        for j in range(2, int(i ** .5) + 1):
            if i % j == 0:
                break
        else:
            count += 1

    return count


# optimal solution
def count_primes_2(n):
    """Using Sieve method is a well-known method in number theory for finding all prime numbers less than a given
    number. It works by creating a list of all numbers from 2 to that given number, and then systematically
    eliminating all the multiples of primes."""
    if n <= 2:
        return 0

    i = 2
    primes = [True] * n
    primes[0] = primes[1] = False

    while i * i < n:
        if primes[i]:
            # mark all the multiples False for the given i
            primes[i * i:n:i] = [False] * len(primes[i * i:n:i])
        i += 1

    return primes.count(True)


# res = count_primes(10)
res = count_primes_2(10)
print(res)
