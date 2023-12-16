def partition_labels(s):
    last_index_dict = {}
    for i, char in enumerate(s):
        last_index_dict[char] = i

    curr_partition_size, max_end = 0, 0
    result = []
    for i, char in enumerate(s):
        curr_partition_size += 1
        max_end = max(max_end, last_index_dict[char])
        # if the current pointer reaches the max end
        if i == max_end:
            result.append(curr_partition_size)
            curr_partition_size = 0

    return result


res = partition_labels('ababcbacadefegdehijhklij')
print(res)
