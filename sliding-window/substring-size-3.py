def substring(s):
    left, right = 0, 3
    count = 0
    curr_window = s[left:right]
    # first window
    if len(set(curr_window)) == 3:
        count += 1

    while right < len(s):
        left += 1
        right += 1
        curr_window = s[left:right]
        if len(set(curr_window)) == 3:
            count += 1

    return count

# constant space solution
def substring_2(s):
    left, right = 0, 2
    count = 0

    while right < len(s):
        # check if all three are distinct
        if s[left] != s[left + 1] and s[left] != s[right] and s[left + 1] != s[right]:
            count += 1
        left += 1
        right += 1

    return count


# res = substring('aababcabc')
res = substring_2('aababcabc')
print(res)
