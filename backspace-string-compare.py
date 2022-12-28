'''Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

'''

class Solution(object):
    
    def backspaceCompare(self, s: str, t: str):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
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

s = "a##c"
t = "#a#c"
soln = Solution()
print(soln.backspaceCompare(s,t))