# this will fail for [1,1,2,2,2,2]
from collections import Counter


def has_group_size_x(deck):
    if len(deck) == 1:
        return False
    counter = {}
    for num in deck:
        if num in counter:
            counter[num] += 1
            continue
        counter[num] = 1

    result = set(counter.values())

    return len(result) == 1


def has_group_size_x_2(deck):
    counter = Counter(deck)
    n = len(deck)
    # need to divide the deck into g equal group
    # array will always be greater than 1 (it is the constraint)
    for g in range(2, n + 1):
        if n % g == 0:
            # the total count of the given number should be divisible by g
            if all(val % g == 0 for val in counter.values()):
                return True

    return False


res = has_group_size_x([1, 2, 3, 4, 4, 3, 2, 1])
print(res)
