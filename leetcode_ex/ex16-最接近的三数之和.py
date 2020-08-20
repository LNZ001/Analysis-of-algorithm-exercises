from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length < 3: return 0
        nums.sort()

        min_dis = float("inf")
        min_pos = None
        for i in range(length-2):
            left = i+1
            right = length-1

            while left < right:
                v = nums[i] + nums[left] + nums[right]
                dis = abs(target - v)
                if dis == 0: return target
                if dis < min_dis:
                    min_dis = dis
                    min_pos = v

                if v > target:
                    right -= 1
                else:
                    left += 1
        return min_pos

if __name__ == '__main__':
    print(Solution().threeSumClosest([-1,2,1,-4], 1))
