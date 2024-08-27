def min_index(list1, list2):
    # create a dict with words and index of list1
    words1_dict = {word: idx for idx, word in enumerate(list1)}
    min_sum = float('inf')
    result = []

    # iterate over the second list and check for same values
    for idx, word2 in enumerate(list2):
        if word2 not in words1_dict:
            continue

        # assign the min value sum between the common words
        if min_sum > idx + words1_dict[word2]:
            min_sum = idx + words1_dict[word2]
            # why assign a new array? coz there will be at least one common word
            result = [word2]
        # also add them when they are the same
        elif min_sum == idx + words1_dict[word2]:
            result.append(word2)

    return result


res = min_index(["happy", "sad", "good"], ["sad", "happy", "good"])
print(res)
