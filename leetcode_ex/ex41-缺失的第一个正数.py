from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = 0
        while pos < len(nums):
            if nums[pos] == pos + 1 or nums[pos] > len(nums) or nums[pos] <= 0:
                pos += 1
            else:
                idx = nums[pos]-1
                nums[pos], nums[idx] = nums[idx], nums[pos]
                if nums[pos] == nums[idx]:
                    pos += 1

        pos = 0
        while pos < len(nums) and nums[pos]-1==pos:
            pos += 1

        return pos+1

if __name__ == '__main__':
    print(Solution().firstMissingPositive([1,1]))