def reverse_words(s):
    arr = s.split(' ')
    count = 0
    result = ''

    for word in arr:
        right = len(word) - 1
        while right >= 0:
            result += word[right]
            right -= 1
        if count < len(arr) - 1:
            result += ' '
        count += 1

    return result


res = reverse_words("Let's take LeetCode contest")
print(res)
