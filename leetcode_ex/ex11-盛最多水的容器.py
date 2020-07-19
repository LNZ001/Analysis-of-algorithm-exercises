from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_v = 0

        while left < right:
            mul_v = min(height[left], height[right]) * (right - left)
            max_v = max(mul_v, max_v)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_v

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))