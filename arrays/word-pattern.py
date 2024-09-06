def word_pattern(pattern, s):
    words = s.split(' ')
    if len(pattern) != len(words):
        return False

    word_to_pattern = {}
    pattern_to_word = {}

    for p, w in zip(pattern, words):
        # case 1: if the given word is already in the dict, and it's value is different
        if w in word_to_pattern and word_to_pattern[w] != p:
            return False
        # case 2: if the given pattern is already in the dict, and it's value is different
        if p in pattern_to_word and pattern_to_word[p] != w:
            return False

        word_to_pattern[w] = p
        pattern_to_word[p] = w

    return True


def word_pattern_2(pattern, s):
    words = s.split(' ')
    # this set creation avoids extra dictionary
    if len(set(pattern)) != len(set(words)):
        return False

    pattern_dict = {}
    curr_idx = 0

    for i in range(len(pattern)):
        if pattern[i] in pattern_dict and pattern_dict[pattern[i]] != words[i]:
            return False
        pattern_dict[pattern[i]] = words[i]
        curr_idx += 1

    return curr_idx == len(words)


# res = word_pattern('abba', 'dog cat cat dog')
res = word_pattern_2('abba', 'dog cat cat dog')
print(res)
