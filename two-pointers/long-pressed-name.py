def long_pressed(name, typed):
    left, right = 0, 0

    while left <= len(name) and right < len(typed):
        # if both are same chars, then move both
        if left < len(name) and name[left] == typed[right]:
            left += 1
            right += 1
        # if they are different, then check if left is not zero and right is still equal to left's prev
        elif right < len(typed) and left != 0 and typed[right] == name[left - 1]:
            right += 1
        else:
            return False

    return left == len(name) and right == len(typed)


res = long_pressed('zlexya', 'aazlllllllllllllleexxxxxxxxxxxxxxxya')
print(res)
