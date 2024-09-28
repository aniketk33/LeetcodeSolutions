import re
from collections import Counter


def most_common(paragraph, banned):
    word_list = []
    symbols = "!?',;."
    for w in paragraph.split(' '):
        curr_word = ''
        for c in w.lower():
            if c.isalpha():
                curr_word += c
            if c in symbols:
                if curr_word:
                    word_list.append(curr_word)
                curr_word = ''
        if curr_word:
            word_list.append(curr_word)

    word_count = Counter(word_list)
    for word, _ in word_count.most_common():
        if word not in banned:
            return word


def most_common_2(paragraph, banned):
    words = re.split(r"\W+", paragraph)
    # to improve the lookup time, we use the set
    banned = set(banned)
    word_count = Counter(list(map(lambda x: x.lower(), words)))

    max_val = 0
    result = ''
    for k, v in word_count.items():
        if k not in banned and v > max_val and k != '':
            max_val = v
            result = k

    return result


# res = most_common("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit'])
# res = most_common('a, a, a, a, b,b,b,c, c', ['a'])
# res = most_common('..Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'])
res = most_common_2('..Bob hit a ball, the hit BALL flew far after it was hit.', ['hit'])
print(res)
