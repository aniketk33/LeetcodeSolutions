from collections import Counter


def max_balloons(text):
    result = len(text)
    count = Counter(text)
    balloon = Counter('balloon')

    for char in balloon:
        # only check for balloon in the given input string
        result = min(result, count[char] // balloon[char])

    return result


res = max_balloons('aniket')
print(res)
