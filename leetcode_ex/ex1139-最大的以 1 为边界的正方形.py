from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        if len(grid)==0: return 0
        if len(grid)==1 and grid[0] == []: return 0

        X = len(grid)
        Y = len(grid[0])

        weights = [[[0]*2 for j in range(Y)] for i in range(X)]

        for i in range(X):
            y_count = 0
            for j in range(Y):
                if grid[i][j] == 0:
                    y_count = 0
                else:
                    y_count += 1
                    weights[i][j][0] = y_count

        for i in range(Y):
            x_count = 0
            for j in range(X):
                if grid[j][i] == 0:
                    x_count = 0
                else:
                    x_count += 1
                    weights[j][i][1] = x_count

        for i in range(X):
            for j in range(Y):
                w = min(weights[i][j])
                if w > 1:
                    while w > 0:
                        if weights[i][j-w+1][1] >= w and weights[i-w+1][j][0] >= w:
                            break
                        w -= 1
                grid[i][j] = w

        return max(max(g) for g in grid) **2

if __name__ == '__main__':
    print(Solution().largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))