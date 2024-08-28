def kth_grammar(n, k):
    rows = ['0']
    if n == 1:
        return int(rows[0][0])
    # 0='01' and 1='10'
    constraints = {'0': '01', '1': '10'}

    for i in range(1, n):
        prev_row = rows[i - 1]
        curr_result = ''

        for char in prev_row:
            curr_result += constraints[char]

        rows.append(curr_result)

    return int(rows[n - 1][k - 1])


def kth_grammar_2(n, k):
    prev_row = '0'
    # 0='01' and 1='10'
    constraints = {'0': '01', '1': '10'}

    for i in range(1, n):
        curr_row = ''

        for char in prev_row:
            curr_row += constraints[char]

        prev_row = curr_row

    return int(prev_row[k - 1])


# using a binary search approach
def kth_grammar_3(n, k):
    # k value will be in between the left and right pointer (given in the problem)
    left, right = 1, 2 ** (n - 1)
    curr_row = 0
    curr_idx = 1

    while curr_idx <= n - 1:
        mid = left + (right - left) // 2
        if k <= mid:
            right = mid
        else:
            # value will remain the same if we are traversing the left side of the tree
            # we need to change the value for the right side
            left = mid + 1
            curr_row = 0 if curr_row == 1 else 1

        curr_idx += 1

    return curr_row


# res = kth_grammar(25, 100)
# res = kth_grammar_2(25, 100)
res = kth_grammar_3(25, 100)
print(res)
