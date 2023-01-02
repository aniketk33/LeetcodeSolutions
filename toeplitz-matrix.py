'''Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

'''
class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        # Initialise Row lenght and Column length
        r_len, c_len = len(matrix),len(matrix[0])
        
        # For every row
        for r in range (1, r_len):
            # For every column
            for c in range (1, c_len):
                # Check if diagonal element are equal or not
                if matrix[r][c]!=matrix[r-1][c-1]:
                    # If diagonal elements are not equal then return False
                    return False
        
        # If for loop is executed it means it satify the condition. Return True
        return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
soln = Solution().isToeplitzMatrix(matrix)
print(soln)