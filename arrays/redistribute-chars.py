from collections import defaultdict


def redistribute(words):
    char_count = defaultdict(int)

    for word in words:
        for c in word:
            char_count[c] += 1

    for k, v in char_count.items():
        if v % len(words) != 0:
            return False

    return True


res = redistribute(["abc", "aabc", "bc"])
print(res)
