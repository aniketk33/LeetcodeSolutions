class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.input_str = s
        self.palindrome_string = self.__to_palindrome_string()
        return self.__check_palindrome()

    def __to_palindrome_string(self):
        char_list = list()
        for chars in self.input_str:
            if chars.isalnum():
                char_list.append(chars.lower())
        
        return ''.join(char_list)

    def __check_palindrome(self):
        return self.palindrome_string == ''.join(reversed(self.palindrome_string))


input = "0P"
s = Solution()
print(s.isPalindrome(input))
# s='nitin:0,'
# s_list = list()
# for i in s:
#     if i.isalnum():
#         s_list.append(i.lower())
# p = ''.join(s_list)
# p_rev = ''.join(reversed(p))
# print(p_rev == p)
# print(p)