from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return 0
        nums.sort()

        res = []
        for i in range(1, len(nums)-1):
            left = i-1
            right = i + 1
            while left >= 0 and right <= len(nums)-1:
                v = nums[left] + nums[right] + nums[i]
                if v == 0:
                    res.append([nums[left], nums[i], nums[right]])
                elif v > 0:
                    left -= 1
                else:
                    right += 1
        return res

if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))