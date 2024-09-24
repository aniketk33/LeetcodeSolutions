# TLE for this approach
def lcp(arr1, arr2):
    prefix = 0
    arr1 = [str(n) for n in arr1]
    arr2 = [str(n) for n in arr2]

    for num1 in arr1:
        for num2 in arr2:
            curr_prefix = 0
            left = right = 0
            while left < len(num1) and right < len(num2) and num1[left] == num2[right]:
                left += 1
                right += 1
                curr_prefix += 1
            if curr_prefix > prefix:
                prefix = curr_prefix

    return prefix


# optimal solution
def lcp_2(arr1, arr2):
    # add all the prefixes from array 2
    prefixes = set()
    for num2 in arr2:
        while num2 > 0:
            prefixes.add(num2)
            num2 = num2 // 10

    prefix_num = 0
    # check if the number from array 1 is the prefix from the set of prefixes
    for num1 in arr1:
        # only calculate the prefix if it is greater than the current prefix
        while num1 > prefix_num:
            if num1 in prefixes:
                if num1 > prefix_num:
                    prefix_num = num1
                break
            num1 = num1 // 10

    if prefix_num == 0:
        return 0

    return len(str(prefix_num))


# res = lcp([10], [17, 11])
res = lcp_2([10], [17, 11])
print(res)
