from collections import defaultdict


def group_anagrams(words):
    # hashmap to store the count of anagrams
    char_count_dict = defaultdict(list)

    for word in words:
        # create a count array to store alphabets for each word
        count = [0] * 26
        for c in word:
            arr_location = ord(c) - ord('a')
            count[arr_location] += 1
        # cannot create list as keys in python op change to tuple
        char_count_dict[tuple(count)].append(word)

    return char_count_dict.values()


def group_anagrams_2(words):
    anagrams = defaultdict(list)

    for word in words:
        # sort the given word and use it as the key
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return anagrams.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# res = group_anagrams(strs)
res = group_anagrams_2(strs)
print(res)
