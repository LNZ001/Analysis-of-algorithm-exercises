from typing import List
'''
方法1， 双指针法, 最后移除
'''

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         left = 0
#         right = 0
#
#         while right < len(nums):
#             if nums[left] != nums[right]:
#                 left += 1
#                 nums[left] = nums[right]
#             right += 1
#
#         for i in range(len(nums)-left-1):
#             nums.pop()
#         return len(nums)

'''
方法二: 双指针直接过程移除.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right=0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left += 1
                right += 1
        return len(nums)

if __name__ == '__main__':
    print(Solution().removeDuplicates([1,1,2]))