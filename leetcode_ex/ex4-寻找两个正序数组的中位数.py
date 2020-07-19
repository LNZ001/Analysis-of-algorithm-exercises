'''
利用找第k小数最容易.
需要把k==1的判定放在最前面, 解决入口就该输出的问题, 避免out of range.
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1 = nums1
        self.nums2 = nums2
        l1 = len(nums1)
        l2 = len(nums2)

        if (l1 + l2)%2 == 0:
            return (self.findK((l1+l2)//2) + self.findK((l1+l2)//2+1))/2
        else:
            return self.findK((l1+l2)//2+1)


    def findK(self, k):
        left = 0
        right = 0
        while True:
            if k == 1: return min(self.nums1[left] if left < len(self.nums1) else float("inf"),
                                  self.nums2[right] if right <len(self.nums2) else float("inf"))

            cut = k//2
            if left + cut > len(self.nums1):
                right += cut
            elif right + cut > len(self.nums2):
                left += cut
            else:
                if self.nums1[left + cut - 1] > self.nums2[right + cut - 1]:
                    right += cut
                else:
                    left += cut
            k -= cut



if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([], [1]))
