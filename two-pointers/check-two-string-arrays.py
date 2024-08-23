def check_valid(word1, word2):
    # pointers for each word
    w1 = w2 = 0
    # pointers for each char in that particular word
    char_w1 = char_w2 = 0

    while w1 < len(word1) and w2 < len(word2):
        # check for mismatch characters
        if word1[w1][char_w1] != word2[w2][char_w2]:
            return False

        char_w1 += 1
        char_w2 += 1

        # check for boundary conditions
        if char_w1 == len(word1[w1]):
            char_w1 = 0
            w1 += 1
        if char_w2 == len(word2[w2]):
            char_w2 = 0
            w2 += 1

    # check if all the words were traversed
    if w1 != len(word1) or w2 != len(word2):
        return False

    return True


res = check_valid(["ab", "c"], ["a", "bc"])
print(res)
