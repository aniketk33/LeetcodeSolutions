def longest_common_prefix(strs):
    if len(strs) == 1:
        return strs[0]

    first_word = strs[0]
    result = ''

    # iterate over the first word and compare it with the other words, char by char
    for i in range(len(first_word)):
        for word in strs:
            if len(word) == i or first_word[i] != word[i]:
                return result

        result += first_word[i]

    return result


arr = ["flower", "flow", "flight"]
res = longest_common_prefix(arr)
print(res)
