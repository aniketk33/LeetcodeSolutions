def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    # create dict for frequency of each char in both the strings
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)  # if the key is not present, then return 0
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False

    return True


original = "rat"
check = "car"
res = valid_anagram(original, check)
print(res)
