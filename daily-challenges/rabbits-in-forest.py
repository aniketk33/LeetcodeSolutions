import math
from collections import Counter


def rabbits(answers: list[int]):
    count = Counter(answers)
    total = 0

    for key, val in count.items():
        # how many others? + myself
        group_size = key + 1
        # how many groups can be formed?
        groups = math.ceil(val / group_size)
        # keep summing up the groups formed
        total += (groups * group_size)

    return total


res = rabbits([10, 10, 10])
print(res)
