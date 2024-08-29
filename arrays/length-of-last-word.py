def last_word(s: str):
    s = s.rstrip()
    word = s.split()[-1]

    return len(word)


def last_word_2(s):
    count, last_idx = 0, len(s) - 1
    # skip all the white spaces from the end
    while last_idx >= 0 and s[last_idx] == ' ':
        last_idx -= 1

    # get to the first char index for the given word
    while last_idx >= 0 and s[last_idx] != ' ':
        count += 1
        last_idx -= 1

    return count


# res = last_word('   fly me   to   the moon  ')
res = last_word_2('   fly me   to   the moon  ')
print(res)
