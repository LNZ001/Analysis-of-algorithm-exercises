from typing import List

# class Solution:
#
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         return [self.find(nums, target, True), self.find(nums, target, False)]
#
#     def find(self, nums, target, isleft=False):
#         left = 0
#         right = len(nums)-1
#
#         mid = (left+right)//2
#
#         while left < right:
#             if nums[mid] > target:
#                 right = mid-1
#             elif nums[mid] == target:
#                 if isleft:
#                     right = mid
#                 else:
#                     left = mid
#                     if right - left == 1:
#                         if nums[right] == target:
#                             left = right
#                         else:
#                             right = left
#                         break
#             else:
#                 left = mid+1
#
#             mid = (left + right) // 2
#
#         if left != right or nums[left] != target: return -1
#         else:
#             return left


'''
34题实现了二分查找的左侧和右侧, 如果没有这个数,找左边界的会到目标值的下一个(略大的), 找右边界的会找左边的.
'''
class Solution:
    def searchRange(self, nums: List[int], target: float) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        start = -1
        end = -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if l < len(nums) and nums[l] == target:
            start = l
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:

                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if r >= 0 and nums[r] == target:
            end = r
        return [start, end]


if __name__ == '__main__':
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
