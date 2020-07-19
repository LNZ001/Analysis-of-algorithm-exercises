'''
背包动态优化.
dp[i][j] 表示只看前i个物品, 总体积是j的情况下 总价值最大是多少.
result = max{f[n][0~V]}

1. 不选第i个, dp[i][j] = dp[i-1][j]
2. 选第i个物品, dp[i][j] = dp[i-1][j-v[i]]

f[i][j]=max{1. 2.}
f[i][0] = 0
f[0][j] = 0

=> 优化1, 一维数组.

恰好为体积j, 就需要初始化特殊处理, 确保是从dp[0]转移来的.
'''

class Solution:

    def bags(self, n, m, v, w):
        dp = [0]*(m+1)
        for i in range(1, len(n)+1):
            for j in range(len(m), 0, -1):
                if j >= v[i]:
                    dp[j] = max(dp[j], dp[j-v[i]] + w[i])

        return dp[m]

if __name__ == '__main__':
    print(Solution().bags(...))



