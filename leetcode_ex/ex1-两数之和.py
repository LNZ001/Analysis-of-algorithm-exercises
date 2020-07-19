'''
暴力求解 和 map存储都可以.
不能重复使用两次,正好一次迭代, 自己和之前的一个.
'''

from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)
        length = len(nums)
        for i in range(length):
            if target - nums[i] in mapp: return [mapp[target - nums[i]], i]

            mapp[nums[i]] = i


if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 4], 6))
