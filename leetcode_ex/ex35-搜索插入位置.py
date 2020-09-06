from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #实际就是二分找左侧位置, 这样, 找不到就是大于的数的第一个的位置, 即插入的位置
        l = 0
        r = len(nums)-1
        mid = l + (r-l)//2
        while l <= r:
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = l + (r-l)//2

        return l


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 5))