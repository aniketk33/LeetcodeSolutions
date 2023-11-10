def last_word(s: str):
    s = s.rstrip()
    word = s.split()[-1]

    return len(word)


res = last_word('   fly me   to   the moon  ')
print(res)
