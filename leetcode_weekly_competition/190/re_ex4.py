from typing import List
class Solution:


    dp = [[-0xfffffff for i in range(501)] for j in range(501)] # 参考复杂度数据length 0-500

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1], self.dp[i-1][j-1] + nums1[i-1]*nums2[j-1],
                                    nums1[i-1]*nums2[j-1])
        return self.dp[len(nums1)][len(nums2)]