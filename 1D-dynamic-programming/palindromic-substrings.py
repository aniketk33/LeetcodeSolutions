def count_palindromes(s):
    def count(left_ptr, right_ptr):
        temp_count = 0
        while left_ptr >= 0 and right_ptr < len(s) and s[left_ptr] == s[right_ptr]:
            temp_count += 1
            left_ptr -= 1
            right_ptr += 1

        return temp_count

    result = 0

    for i in range(len(s)):
        # odd length
        result += count(i, i)
        # even length
        result += count(i, i + 1)

    return result


res = count_palindromes('abc')
print(res)
