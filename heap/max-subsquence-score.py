import heapq


def max_score(nums1, nums2, k):
    sorted_pairs = [(i, j) for i, j, in zip(nums1, nums2)]
    # sort the pairs with values from the second list in descending order
    sorted_pairs = sorted(sorted_pairs, key=lambda x: x[1], reverse=True)

    result = 0
    min_heap = []
    nums1_sum = 0

    for n1, n2 in sorted_pairs:
        nums1_sum += n1
        heapq.heappush(min_heap, n1)

        # check if it exceeds k and remove the lowest from the heap
        if len(min_heap) > k:
            n1_pop = heapq.heappop(min_heap)
            nums1_sum -= n1_pop

        # if it equals k then apply the formula
        if len(min_heap) == k:
            result = max(result, nums1_sum * n2)

    return result


res = max_score([1, 3, 3, 2], [2, 1, 3, 4], 3)
print(res)
