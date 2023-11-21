def max_vowel(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    left_ptr, right_ptr = 0, 0
    result = 0
    curr_count = 0

    while right_ptr < len(s):
        if s[right_ptr] in vowels:
            curr_count += 1

        # check if the window size is greater than the threshold
        if right_ptr - left_ptr + 1 > k:
            # decrement only when it is not a vowel
            if s[left_ptr] in vowels:
                curr_count -= 1
            left_ptr += 1

        result = max(result, curr_count)
        right_ptr += 1

    return result


res = max_vowel("aeiou", 2)
print(res)
