def k_beauty(num, k):
    left, right = 0, k
    count = 0
    s = str(num)

    while right <= len(s):
        curr_window = s[left:right]
        if int(curr_window) and num % int(curr_window) == 0:
            count += 1
        left += 1
        right += 1

    return count


res = k_beauty(430043, 2)
print(res)
