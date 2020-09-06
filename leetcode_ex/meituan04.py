from typing import List


class Solution:

    def rindex(self, key, n, n_list):
        for i in range(n-1, -1, -1):
            if n_list[i] == key:
                return i
        else:
            return None


    def work(self,m, n, n_list):
        dp = []*n
        max_left = []*n

        for i in range(n):
            if i == 0:
                max_left[i] = 0
            else:
                max_left[i] = max(max_left[i-1], n_list[i-1])

        for i in range(n):
            k = self.rindex(i+1, n, n_list)
            dp[i] = None if k is None or max_left[k] <= i+1 else max_left[k]

        max_v = 0
        count = 0
        for i in range(m):
            if dp[i] is None:
                pass
            else:
                max_v = max(max_v, dp[i])

            count += (n - max_v + 1)


if __name__ == '__main__':
    print(Solution().work())