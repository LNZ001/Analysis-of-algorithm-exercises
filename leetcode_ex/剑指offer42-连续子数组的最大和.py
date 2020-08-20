from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        # ########## dp[i] 记录能够到达该位置的最大和 ##########
        dp = [0]*len(nums)

        for i in range(len(nums)):
            dp[i] = dp[i-1] + nums[i] if i-1>=0 and dp[i-1] > 0 else nums[i]

        return max(dp)

if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

