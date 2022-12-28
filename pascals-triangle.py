class Solution:
    def generate(self, numRows: int):
        parent_list = []
        for i in range(numRows):
            temp_list = []
            for j in range(i+1):
                if j == 0 or len(parent_list) == j:
                    temp_list.append(1)
                    if i == j:
                        parent_list.append(temp_list)
                    continue
                if len(parent_list) > 0:
                    last_element = parent_list[-1]
                    temp_list.append(last_element[j-1] + last_element[j])
        
        return parent_list


numRows = 5
soln = Solution().generate(numRows)
print(soln)