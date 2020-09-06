'''
参考版本: [快速排序](https://blog.csdn.net/weixin_43250623/article/details/88931925)
'''

class Solution:

    def quicksort(self, nums, l=0, r=None):
        if r is None: r = len(nums)-1
        if l >= r: return
        start = l
        end = r

        pivot = nums[l]
        while l < r:
            while nums[r] >= pivot and l < r:
                r -= 1
            nums[l] = nums[r]

            while nums[l] <= pivot and l < r:
                l += 1
            nums[r] = nums[l]

        nums[l] = pivot
        self.quicksort(nums, start, l-1)
        self.quicksort(nums, l+1, end)
        return nums

if __name__ == '__main__':
    print(Solution().quicksort([3, 4, 5, 2, 6, 1]))