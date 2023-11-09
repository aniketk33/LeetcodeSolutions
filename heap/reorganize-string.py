import heapq
from collections import Counter


def reorganize_string(s):
    result = ''

    # create the char count hashmap
    count_dict = Counter(s)

    # initialize the max heap
    max_heap = [[-count, char] for char, count in count_dict.items()]
    heapq.heapify(max_heap)

    prev_val = None

    while prev_val or max_heap:
        # check if prev_val is still present, but max_heap is empty then return an empty string
        if not max_heap and prev_val:
            return ''

        # pop the most frequent char from the heap
        count, freq_char = heapq.heappop(max_heap)
        result += freq_char
        count += 1

        # if there exists a prev val, then add back to the heap
        # and re-initialize to None
        if prev_val:
            heapq.heappush(max_heap, prev_val)
            prev_val = None

        if count != 0:
            prev_val = [count, freq_char]

    return result


res = reorganize_string('aab')
print(res)
