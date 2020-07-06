from typing import List

class Solution:
    def numTrees(self, n: int) -> int:

        dp = [1] + [0]*n
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]


if __name__ == '__main__':
    print(Solution().numTrees(3))