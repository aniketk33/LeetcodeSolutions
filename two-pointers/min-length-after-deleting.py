def min_length(s):
    left, right = 0, len(s) - 1
    result = len(s)

    # they should not intersect, so not less than equal
    while left < right:
        if s[left] != s[right]:
            return result
        # move the left pointer to a new character
        while left <= right and s[left] == s[right]:
            left += 1

        # move the right pointer to a new character.
        # why left - 1? as it will be shifted towards a new char position,
        # so the old char will be just before the new one
        while left <= right and s[left - 1] == s[right]:
            right -= 1

        result = min(result, right - left + 1)

    return result if result >= 0 else 0


# much better and cleaner approach
def min_length_2(s):
    left, right = 0, len(s) - 1

    # they should not intersect, so not less than equal and have to be equal all the time
    while left < right and s[left] == s[right]:
        temp = s[left]
        # move the left pointer to a new character
        while left <= right and s[left] == temp:
            left += 1

        # move the right pointer to a new character
        while left <= right and s[right] == temp:
            right -= 1

    return right - left + 1


res = min_length('aba')
print(res)
