def binary_codes(s, k):
    combination_sets = set()

    for i in range(len(s) - k + 1):
        combination_sets.add(s[i:i + k])

    return len(combination_sets) == 2 ** k


res = binary_codes('00110110', 2)
print(res)
