def first_palindrome(words):
    def is_palindrome(w):
        left, right = 0, len(w) - 1
        while left <= right:
            if w[left] != w[right]:
                return False
            left += 1
            right -= 1

        return True

    for word in words:
        if is_palindrome(word):
            return word

    return ''


res = first_palindrome(["abc", "car", "ada", "racecar", "cool"])
print(res)
