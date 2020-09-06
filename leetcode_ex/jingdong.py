from typing import List
from collections import Counter

class Solution:

    def check(self, n, m, n_list):
        mapp = Counter(n_list)
        f = list(mapp.keys())
        f.sort()

        dp = [0]*(m+1)
        dp[0] = 1

        for i in range(1, m+1):
            for k in f:
                if i-k >= 0:
                    dp[i] += dp[i-k] * mapp[k]
                else:
                    break

        return dp[m]

if __name__ == '__main__':
    print(Solution().check(3, 10, [1, 2, 2]))


