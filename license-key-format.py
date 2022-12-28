class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:        
        # null check
        if s is None:
            return None

        # forming a simple string by removing the dashes
        without_dashed = ''.join(s.split('-'))
        temp = len(without_dashed) 

        # making equal groups of the simple string (in order to place the dash)
            # the first group can be less than or equal to 'k' but cannot be 0        
        temp = temp % k
        if temp == 0:
            list_str = list(without_dashed)
            for i in range(int(len(without_dashed)/k) - 1):
                list_str.insert(k, '-')
                k  = k + k + 1
            return ''.join(list_str).upper()
        else:
            list_str = list(without_dashed)
            for i in range(int(len(without_dashed)/k)):
                if i == 0:
                    list_str.insert(temp,'-')
                    k = k + temp + 1
                    continue
                list_str.insert(k, '-')
                k = k + k + 1
            return ''.join(list_str).upper()

input_key = '2-5g-3-J'
input_len = 2
soln = Solution().licenseKeyFormatting(input_key, input_len)
print(soln)