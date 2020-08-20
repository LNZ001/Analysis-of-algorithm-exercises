from typing import List
import bisect

class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # ########## 倒排. ##########
        if nums is None or len(nums) == 1: return nums

        length = len(nums)
        for i in range(length-1, 0, -1):
            if nums[i] <= nums[i-1]: continue

            # ########## 还存在更大的数 ##########
            tmp = nums[i:]
            tmp.reverse()
            index = bisect.bisect_right(tmp, nums[i-1])
            index = len(nums)-1 - index
            nums[i-1], nums[index] = nums[index], nums[i-1]
            left = i
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return
        else:
            nums.reverse()
            return

if __name__ == '__main__':
    nums=[1, 2, 6, 6, 5]
    print(Solution().nextPermutation(nums))
    print(nums)
