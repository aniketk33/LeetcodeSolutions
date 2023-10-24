def palindrome_partitioning(input_str):
    result = []

    def is_palindrome(left_ptr, right_ptr):
        while left_ptr < right_ptr:
            if input_str[left_ptr] != input_str[right_ptr]:
                return False
            left_ptr, right_ptr = left_ptr + 1, right_ptr - 1

        return True

    def dfs(curr_idx, curr_partitions):
        # base case
        if curr_idx >= len(input_str):
            result.append(curr_partitions[:])
            return

        for i in range(curr_idx, len(input_str)):
            if is_palindrome(left_ptr=curr_idx, right_ptr=i):
                curr_partitions.append(input_str[curr_idx:i + 1])
                dfs(i + 1, curr_partitions)
                curr_partitions.pop()

    dfs(0, [])
    return result


s = 'aabb'
res = palindrome_partitioning(s)
print(res)
