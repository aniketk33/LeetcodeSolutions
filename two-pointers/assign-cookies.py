def assign(children, cookies):
    children.sort()
    cookies.sort()
    left, right = 0, 0
    while left < len(children) and right < len(cookies):
        # move until you find a valid cookie
        while right < len(cookies) and children[left] > cookies[right]:
            right += 1

        # check if right is in bound
        if right == len(cookies):
            break
        # if smaller one found then increment both the pointers
        left += 1
        right += 1

    return left


# res = assign([10, 9, 8, 7], [5,6,7,8])
res = assign([1, 2, 3], [1, 1])
print(res)
