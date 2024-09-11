from collections import Counter


def find_words(words, chars):
    chars_count = Counter(chars)
    word_count = 0

    for word in words:
        result = ''
        chars_count_copy = chars_count.copy()
        for c in word:
            if c not in chars_count or chars_count_copy[c] < 1:
                break
            chars_count_copy[c] -= 1
            result += c
        if result == word:
            word_count += len(word)

    return word_count


res = find_words(["cat", "bt", "hat", "tree"], 'atach')
print(res)
