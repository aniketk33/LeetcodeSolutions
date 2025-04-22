def count_hidden(differences, lower, upper):
    n = len(differences)
    # the hidden array is of size n+1
    hidden_array = [0] * (n + 1)
    prefix_sum = 0
    for idx, diff in enumerate(differences):
        hidden_array[idx] += prefix_sum
        prefix_sum += diff

    # for the last element
    hidden_array[n] += prefix_sum
    # x and y are the max and min value of the hidden array
    x, y = max(hidden_array), min(hidden_array)

    total_sequences = (upper - lower - (x - y) + 1)
    return total_sequences if total_sequences > 0 else 0


res = count_hidden([1, -3, 4], 1, 6)
print(res)
