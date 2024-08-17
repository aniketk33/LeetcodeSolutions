def compression(chars):
    left, right = 0, 0

    while right < len(chars):
        count = 1
        while right < len(chars) - 1 and chars[right] == chars[right + 1]:
            right += 1
            count += 1

        chars[left] = chars[right]
        left += 1
        if count > 1:
            for c in str(count):
                chars[left] = c
                left += 1
        # to start from the next new character
        right += 1

    return left


# edge case
res = compression(["a", "a", "a", "b", "b", "a", "a"])
# res = compression(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
print(res)
