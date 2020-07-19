from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        wid = len(grid[0])
        height = len(grid)

        widths = [0] * wid
        heights = [0] * height

        for i in range(wid):
            for j in range(height):
                widths[i] += grid[j][i]
                heights[j] += grid[j][i]

        count = 0
        for i in range(wid):
            for j in range(height):
                if grid[j][i] == 1 and (widths[i] >= 2 or heights[j] >= 2):
                    count += 1

        return count


if __name__ == '__main__':
    print(Solution().countServers([[1,0],[1,1]]))