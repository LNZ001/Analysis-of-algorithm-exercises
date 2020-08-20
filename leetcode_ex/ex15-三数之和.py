from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 3: return []
        nums.sort()

        result = []
        last_n = None
        for i in range(length-2):
            if last_n is not None and last_n == nums[i]:
                continue
            else:
                last_n = nums[i]

            left = i+1
            right = length-1
            while left < right:
                v = nums[left] + nums[right] + nums[i]
                if v == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    tmp_left = nums[left]
                    tmp_right = nums[right]
                    left += 1
                    right -= 1
                    while left < right and tmp_left == nums[left] and tmp_right == nums[right]:
                        left += 1
                        right -= 1
                elif v > 0:
                    right -= 1
                else:
                    left += 1

        return result

if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))