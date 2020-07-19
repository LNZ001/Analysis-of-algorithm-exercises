'''

max({f[0...m]})
'''

from typing import List

def bags(n, m, v, w):

    dp = [0] * (m+1)

    for j in range(1, m+1):
        for i in range(n):
            if j>=v[i]:
                dp[j] = max(dp[j], dp[j-v[i]] + w[i])

    return max(dp)


if __name__ == '__main__':
    bags(...)