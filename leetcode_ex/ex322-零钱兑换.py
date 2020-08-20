from typing import List
from queue import Queue
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp = [-1]*(amount+1)
        # dp[0] = 0
        #
        # for i in range(1, amount+1):
        #     for c in coins:
        #         if i - c >= 0 and dp[i-c] != -1:
        #             if dp[i] == -1:
        #                 dp[i] = dp[i-c] + 1
        #             else:
        #                 dp[i] = min(dp[i-c] + 1, dp[i])
        # return dp[amount]


        # n = len(coins)
        # coins.sort(reverse=True)
        # self.res = float("inf")
        #
        # def dfs(index, target, count):
        #     coin = coins[index]
        #     # if count>self.res:
        #     #     return
        #     if math.ceil(target / coin) + count >= self.res:
        #         return
        #     if target % coin == 0:
        #         self.res = count + target // coin
        #     if index == n - 1: return
        #     for j in range(target // coin, -1, -1):
        #         dfs(index + 1, target - j * coin, count + j)
        #
        # dfs(0, amount, 0)
        #
        # return int(self.res) if self.res != float("inf") else -1

        n = len(coins)
        coins.sort(reverse=True)
        self.res = float("inf")

        def dfs(index, target, count):
            if index >= n: return
            coin = coins[index]
            if math.ceil(target/coin) + count >= self.res:
                return
            if target%coin == 0:
                self.res = count + target//coin
                return
            if target//coin == 0:
                dfs(index + 1, target, count)
            else:
                for i in range(target//coin, -1, -1):
                    dfs(index+1, target - i * coin, count + i)


        dfs(0, amount, 0)
        return int(self.res) if self.res != float("inf") else -1


if __name__ == '__main__':
    print(Solution().coinChange(coins = [1, 2, 5], amount = 11))