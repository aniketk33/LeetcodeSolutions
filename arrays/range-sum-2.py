from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows, columns = len(matrix), len(matrix[0])
        # create the prefix matrix filled with 0s covering the boundary cases by adding extra row and column
        self.prefix_matrix = [[0] * (columns + 1) for _ in range(rows + 1)]

        for row in range(rows):
            prefix_sum = 0
            for col in range(columns):
                prefix_sum += matrix[row][col]
                above = self.prefix_matrix[row][col + 1]
                self.prefix_matrix[row + 1][col + 1] = prefix_sum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # excluding the boundary as they are 0s
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2
        bottom_right = self.prefix_matrix[row2][col2]
        left = self.prefix_matrix[row2][col1 - 1]
        above = self.prefix_matrix[row1 - 1][col2]
        top_left = self.prefix_matrix[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
