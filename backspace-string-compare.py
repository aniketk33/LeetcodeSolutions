"""Given two strings s and t, return true if they are equal when both are typed into empty text editors.'#' means a
backspace character.

Note that after backspacing an empty text, the text will continue empty.

"""


# Naive solution
class Solution(object):

    def __init__(self):
        self.first_str = None
        self.second_str = None

    def backspaceCompare(self, s: str, t: str):
        self.first_str = s
        self.second_str = t

        result_first_str = self.__first_str()
        result_second_str = self.__second_str()

        return result_first_str == result_second_str

    def __first_str(self):
        result_list = list()
        for chars in self.first_str:
            if chars == '#':
                if len(result_list) == 0:
                    continue
                result_list.pop()
            else:
                result_list.append(chars)

        return ''.join(result_list)

    def __second_str(self):
        result_list = list()
        for chars in self.second_str:
            if chars == '#':
                if len(result_list) == 0:
                    continue
                result_list.pop()
            else:
                result_list.append(chars)

        return ''.join(result_list)


# time and space complexity is O(n)
def back_space(s, t):
    result1, result2 = [], []
    # for string 1
    for c1 in s:
        if c1 == '#':
            if result1:
                result1.pop()
        else:
            result1.append(c1)
    # for string 2
    for c2 in t:
        if c2 == '#':
            if result2:
                result2.pop()
        else:
            result2.append(c2)

    return result1 == result2


# optimal approach
def back_space_2(s, t):
    def next_valid_char(input_str, curr_idx):
        # counting the number of hashtags
        hashtag_count = 0

        while curr_idx >= 0:
            # check if there are no hashtags and current char is a valid char
            if hashtag_count == 0 and input_str[curr_idx] != '#':
                break
            if input_str[curr_idx] == '#':
                hashtag_count += 1
            else:
                hashtag_count -= 1
            curr_idx -= 1

        return curr_idx

    index_s, index_t = len(s) - 1, len(t) - 1

    while index_s >= 0 or index_t >= 0:
        # reassign the values of next valid index
        index_s = next_valid_char(s, index_s)
        index_t = next_valid_char(t, index_t)

        # if index is out of bound, then assign an empty string
        result_s = s[index_s] if index_s >= 0 else ''
        result_t = t[index_t] if index_t >= 0 else ''

        if result_s != result_t:
            return False

        index_s -= 1
        index_t -= 1

    return True


s1 = "a##c"
t1 = "#a#c"
# solution = Solution()
# print(solution.backspaceCompare(s1, t1))
# res = back_space(s1, t1)
res = back_space_2(s1, t1)
print(res)
