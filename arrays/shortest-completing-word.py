from collections import defaultdict


def shortest_word(license_plate: str, words: list):
    # get the frequency of check string
    check_string_dict = defaultdict(int)
    for c in license_plate:
        if c.isalpha():
            check_string_dict[c.lower()] += 1

    result = ''
    min_len = float('inf')

    for word in words:
        # get the frequency count for each char in the current word
        curr_char_dict = defaultdict(int)
        for c in word:
            curr_char_dict[c] += 1
        valid_string = True
        # check if any of the current char frequency is less than check char frequency
        for char, val in check_string_dict.items():
            if (char in curr_char_dict and curr_char_dict[char] < val) or char not in curr_char_dict:
                valid_string = False
                break

        if valid_string:
            # store the shortest value
            if min_len > len(word):
                result = word
                min_len = len(word)

    return result


res = shortest_word("1s3 456", ["looks", "pest", "stew", "show"])
print(res)
