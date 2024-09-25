"""1.Two strings are said to be similar if they are composed of the same characters. For example, "abaca" and "cba"
are similar since both of them are composed of characters 'a', 'b' and 'c'. However, "abaca" and "bcd" are not
similar since they do not share all the same letters. Given an array of strings words of length n, find the number
of pairs of strings that are similar. Note: • Each string is composed of lowercase English characters only. • Pairs
are considered index-wise, i.e., two equal strings at different indices are counted as separated pairs. • A pair at
indices (i, j) is the same as the pair at (, i). Example Consider n = 3, words = ["xyz", "foo", "of"]. Here,
the strings "foo" and "of" are similar because they are composed of the same characters ['o', 'f']. There are no
other similar pairs, so the answer is 1.

Words = ["aba", "abaca", "baab", "cba"]
output = 2
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

"""2. In a neural network, there are n layers, each with computational time represented by the array 
computationalTime. Developers are provided with an operation where they can select all layers with computation time 
c, an even integer. They then adjust parameters, reducing the processing time of these layers from cto c / 2. The 
task is to determine the minimum number of operations needed to ensure that the computational time of all layers is 
odd. Example n=4 computationalTime = [2, 4, 8, 16] The optimal approach is: • Choose c = 16 and reduce the 
computation time of layer 4 to 8. Thus, computationalTime = [2, 4, 8, 8]. • Choose c = 8 and reduce the computation 
time of layers 3 and 4 to 4. Thus, computationalTime = [2, 4, 4, 4]. • Choose c = 4 and reduce the computation time 
of layers 2, 3 and 4 to 2. Thus, computationalTime = [2, 2, 2, 2]. • Choose c = 2 and reduce the computation time of 
all the layers to 1. Thus, computationalTime = [1, 1, 1, 1]. The number of operations applied = 4. Thus, the answer 
returned is 4."""


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
