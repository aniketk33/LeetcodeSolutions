"""
I had to write a functions to return the number of similar words. For example, words = ["xyz", "foo", "of"].
Here, the strings "foo" and "of" are similar because they are composed of the same characters 'o' and 'f'
"""
from collections import defaultdict
from heapq import heapify, heappop, heappush


# brute force approach. TLE
def count_pairs(words):
    count = 0

    # compare each word with the remaining words
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if set(words[i]) == set(words[j]):
                count += 1

    return count


def count_pairs_2(words):
    count = 0
    # create a dict for unique strings and their count
    unique_dict = defaultdict(int)
    for word in words:
        curr_str = ''.join(sorted(set(word)))
        unique_dict[curr_str] += 1

    # only calculate the pairs for values greater than 1
    for key, val in unique_dict.items():
        if val > 1:
            count += val * (val - 1) // 2

    return count


# res1 = count_pairs(["xyz", "foo", "of"])
res1 = count_pairs_2(["aba", "abaca", "baab", "cba"])
print(res1)

"""
I need to make the array with all odd computation time by performing operations on the max element first and 
divide it into half everytime. For example, computationalTime = [2, 4, 8, 16] 
1st iteration: consider 16, so it will become [2, 4, 8, 8], 
2nd iteration: consider 8 -> [2,4,4,4], 
next consider 4 -> [2,2,2,2]
finally consider 2 -> [1,1,1,1]. All the values are odd, return the count of operations required to make them odd. 
"""


def count_operations(computation_time):
    # create a max heap of unique time
    unique_nums = set(computation_time)
    max_heap = [-t for t in unique_nums]
    heapify(max_heap)

    count = 0

    while len(max_heap) > 0:
        val = -1 * heappop(max_heap)
        # only perform operation on even values
        if val % 2 == 0:
            count += 1
            val = val // 2
            if val not in unique_nums and val % 2 != 0:
                unique_nums.add(val)
                heappush(max_heap, -val)

    return count


res2 = count_operations([2, 4, 8, 16])
print(res2)
