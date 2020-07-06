from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        lens_x = len(matrix)
        lens_y = len(matrix[0])

        dp_matrix = [[0] + i for i in matrix]
        dp_matrix.insert(0, [0] * (lens_y+1))
        max_matrix = 0
        for i in range(1, lens_x + 1):
            for j in range(1, lens_y + 1):
                dp_matrix[i][j] = int(dp_matrix[i][j])
                if dp_matrix[i][j] == 0:
                    continue

                # dp_matrix[i][j] 为 1
                dp_matrix[i][j] = min(min(dp_matrix[i-1][j], dp_matrix[i][j-1]), dp_matrix[i-1][j-1]) + 1

                max_matrix = max(max_matrix, dp_matrix[i][j])
        return max_matrix



if __name__ == '__main__':
    print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))