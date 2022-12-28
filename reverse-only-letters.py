from string import ascii_uppercase, ascii_lowercase


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        final_str = ''
        temp_str = ''
        non_letters_dict = dict()

        # return none if empty or null
        if s is None:
            return final_str
                    
        # store non-letters in dict with keys as the index
        index = 0
        for i in s:
            try:
                if i in ascii_lowercase  or i in ascii_uppercase:
                    temp_str += i
                    continue
                non_letters_dict[index] = i
            finally:
                index += 1

        # reverse the letters
        reversed_str = list(reversed(temp_str))        

        # insert the non-letters at the given index
        for k,v in non_letters_dict.items():
            reversed_str.insert(k,v)

        # return the final string
        return final_str.join(reversed_str)        

input_str = 'Test1ng-Leet=code-Q!'
soln = Solution().reverseOnlyLetters(input_str)
print(soln)