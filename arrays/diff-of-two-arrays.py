def diff(nums1, nums2):
    # diff1, diff2 = [], []
    #
    # for n1 in nums1:
    #     if n1 in nums2 or n1 in diff1:
    #         continue
    #     diff1.append(n1)
    #
    # for n2 in nums2:
    #     if n2 in nums1 or n2 in diff2:
    #         continue
    #     diff2.append(n2)
    #
    # return [diff1, diff2]

    # Using HastSet, the time complexity for searching an element is in constant time
    # Runtime is also improved compared to the above solution
    nums1set, nums2set = set(nums1), set(nums2)
    # to prevent adding duplicates
    diff1, diff2 = set(), set()

    # add the distinct elements
    for n1 in nums1set:
        if n1 not in nums2set:
            diff1.add(n1)
    for n2 in nums2set:
        if n2 not in nums1set:
            diff2.add(n2)

    return [list(diff1), list(diff2)]


res = diff([1, 2, 3], [2, 4, 6])
print(res)
