# return True or False if the string is palindrome or not if we remove a char
def is_palindrome(s):
    left_ptr, right_ptr = 0, len(s) - 1

    while left_ptr < right_ptr:
        if s[left_ptr] != s[right_ptr]:
            # excluding the left
            skip_left = s[left_ptr + 1: right_ptr + 1]
            # excluding the right
            skip_right = s[left_ptr:right_ptr]
            # reverse the removed character string
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

        left_ptr += 1
        right_ptr -= 1

    return True


res = is_palindrome('abca')
print(res)
