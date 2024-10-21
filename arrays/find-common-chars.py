from collections import Counter


def find_common(words):
    # chars of the first word should be present in all the words
    count_char = Counter(words[0])

    for word in words[1:]:
        curr_freq = Counter(word)
        for c in list(count_char.keys()):
            if c in curr_freq:
                # get the min value
                count_char[c] = count_char[c] if curr_freq[c] > count_char[c] else curr_freq[c]
            else:
                # remove the char which is not common in the list
                del count_char[c]

    result = []
    for k, v in count_char.items():
        result += ([k] * v)

    return result


res = find_common(["bella", "label", "roller"])
print(res)
