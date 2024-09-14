def min_changes(s):
    # if it starts with 0
    count = 0

    for i in range(len(s)):
        if i % 2 == 0:
            count += 1 if s[i] == '1' else 0
        else:
            count += 1 if s[i] == '0' else 0

    return count if len(s) - count > count else len(s) - count


res = min_changes('0100')
print(res)
