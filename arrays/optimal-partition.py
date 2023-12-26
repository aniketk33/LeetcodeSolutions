def optimal_partition(s):
    result = 1
    duplicates = set()

    for char in s:
        # reset the counter
        if char in duplicates:
            result +=1
            duplicates.clear()
        duplicates.add(char)

    return result


res = optimal_partition('abac')
print(res)
