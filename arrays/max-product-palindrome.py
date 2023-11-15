# need a revision on this problem
def max_product(s):
    result = 0

    def is_palindrome(curr_str):
        left_ptr, right_ptr = 0, len(curr_str) - 1
        while left_ptr < right_ptr:
            if curr_str[left_ptr] != curr_str[right_ptr]:
                return False
            left_ptr, right_ptr = left_ptr + 1, right_ptr - 1

        return True

    def dfs(curr_idx, a, b):
        nonlocal result
        if curr_idx >= len(s):
            if is_palindrome(a) and is_palindrome(b):
                result = max(result, len(a) * len(b))
            return

        a.append(s[curr_idx])
        dfs(curr_idx + 1, a, b)
        a.pop()

        b.append(s[curr_idx])
        dfs(curr_idx + 1, a, b)
        b.pop()

        dfs(curr_idx + 1, a, b)

    dfs(0, [], [])
    return result


res = max_product('leetcodecom')
print(res)
