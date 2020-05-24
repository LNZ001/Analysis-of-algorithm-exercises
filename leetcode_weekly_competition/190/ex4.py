import math
from typing import List


class Solution:

    # # 动态规划？
    # def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
    dp = [[-0xfffffff for i in range(501)] for j in range(501)]

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                self.dp[i][j] = max(
                    [self.dp[i][j - 1], self.dp[i - 1][j], self.dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],
                     nums1[i - 1] * nums2[j - 1]])
        return self.dp[len1][len2]


if __name__ == '__main__':
    tuple_list = [
        ([2,1,-2,5],[3,1,-6]),
        ([3,-2],[2,-6,7]),
        ([-1,-1],[1,1]),
        ([1, -1, 100, 1], [2,3 ,5])

    ]
    for t in tuple_list:
        print(Solution().maxDotProduct(*t))