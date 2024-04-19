import heapq


def top_k_frequent(num_arr, k):
    result = []
    # create dict to store frequency
    count = {}
    # create the frequency table
    frequency_table = [[] for _ in range(len(num_arr) + 1)]

    for num in num_arr:
        count[num] = 1 + count.get(num, 0)

    for num, count in count.items():
        frequency_table[count].append(num)

    for i in range(len(frequency_table) - 1, 0, -1):
        for num in frequency_table[i]:
            result.append(num)
            if len(result) == k:
                return result


def top_k_frequent_2(nums, k):
    """using heaps"""
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # store the negative count for each num
    max_heap = []
    for key, val in count.items():
        max_heap.append((-val, key))

    heapq.heapify(max_heap)
    result = []
    while k > 0:
        # store the key in the result array
        result.append(heapq.heappop(max_heap)[1])
        k -= 1

    return result


arr = [1, 1, 1, 2, 2, 3]
k = 2
res = top_k_frequent_2(arr, k)
print(res)
