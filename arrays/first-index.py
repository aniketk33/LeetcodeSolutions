def first_idx(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1


res = first_idx('le', 'sad')
print(res)
