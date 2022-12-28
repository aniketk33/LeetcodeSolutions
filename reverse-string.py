'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

'''

class Solution:
    def reverseString(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        list_len = len(s)
        print(list_len)
        list_len = list_len//2 + 1 if list_len % 2 != 0 else list_len//2
        last_index = -1
        for i in range(list_len):
            print(last_index, list_len, i)
            first_element = s[i]
            s[i] = s[last_index]
            s[last_index] = first_element
            last_index -= 1
        return s

input = ['a','n','i','k','e','t']
soln = Solution().reverseString(input)
print(soln)