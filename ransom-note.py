from collections import Counter


def ransom_note(ransomNote, magazine):
    mag = Counter(magazine)

    for c in ransomNote:
        if c not in mag or mag[c] < 1:
            return False
        mag[c] -= 1

    return True


res = ransom_note('aa', 'ab')
print(res)
