from collections import Counter


def first_unique(s):
    count = Counter(s)

    for i, c in enumerate(s):
        if count[c] == 1:
            return i

    return -1


res = first_unique('aabb')
print(res)
