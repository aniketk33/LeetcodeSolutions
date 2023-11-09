import heapq


def happy_string(a_count, b_count, c_count):
    result = ''

    # create max_heap
    max_heap = []
    for char, count in [('a', -a_count), ('b', -b_count), ('c', -c_count)]:
        # skip if count is zero
        if count == 0:
            continue
        heapq.heappush(max_heap, (count, char))

    while max_heap:
        count, freq_char = heapq.heappop(max_heap)

        # check if last two char are the same and the length is greater than 1
        if len(result) > 1 and result[-1] == result[-2] == freq_char:
            # if the next frequent char does not exist, then break from the loop and return the result
            if not max_heap:
                break
            # then find the next frequent character
            count_2, freq_char_2 = heapq.heappop(max_heap)
            result += freq_char_2
            count_2 += 1

            # Add to the heap if the count is not equal to 0
            if count_2 != 0:
                heapq.heappush(max_heap, (count_2, freq_char_2))
        else:
            # add the frequent char to the result
            result += freq_char
            count += 1

        # add the frequent char back to the heap if the count is not 0
        if count != 0:
            heapq.heappush(max_heap, (count, freq_char))

    return result


res = happy_string(1, 1, 7)
print(res)
