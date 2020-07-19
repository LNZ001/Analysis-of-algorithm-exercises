'''
要点:
动态规划声明:
dp = [[False] * (len(p)+1) for i in range(len(s)+1)]
dp[0][0] = True
for i in range(1, len(s)+1):
    dp[i][0] = False
for i in range(len(s)+1):
    for j in range(1, len(p)+1):
        ...
        //每一种情况都需要考虑起始位置.
return dp[len(s)][len(p)]
'''

from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for i in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(1, len(s)+1):
            dp[i][0] = False

        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1] if i-1>= 0 else False
                elif p[j-1] == "*":

                    # ########## 先看空匹配. ##########
                    if dp[i][j-2]:
                        dp[i][j] = True
                        continue
                    if i == 0:
                        continue
                    # ########## 递减. ##########
                    cur = i-1
                    while cur >= 0 and (s[cur] == p[j-2] or p[j-2] == "."):
                        if dp[cur][j-2]:
                            dp[i][j] = True
                            break
                        cur -= 1

                else:
                    dp[i][j] = dp[i-1][j-1] if i>=1 and j>=1 and s[i-1] == p[j-1] else False

        return dp[len(s)][len(p)]

if __name__ == '__main__':
    print(Solution().isMatch("" ,"c*"))