def valid_palindrome(sentence: str):
    char_arr = list(sentence)
    char_arr_len = len(char_arr)
    if char_arr_len <= 1:
        return True

    left_ptr, right_ptr = 0, char_arr_len - 1
    while right_ptr >= left_ptr:
        # skip if we encounter any alphanumeric chars
        if not char_arr[left_ptr].isalnum():
            left_ptr += 1
            continue
        if not char_arr[right_ptr].isalnum():
            right_ptr -= 1
            continue
        if char_arr[left_ptr].lower() != char_arr[right_ptr].lower():
            return False
        left_ptr += 1
        right_ptr -= 1

    return True


s = "A man, a plan, a canal: Panama"
res = valid_palindrome(s)
print(res)
