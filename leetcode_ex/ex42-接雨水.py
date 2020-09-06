from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        i = 0
        ans = 0
        while i < len(height):

            while len(stack) != 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                ans += distance * bounded_height

            stack.append(i)
            i += 1
        return ans


class Solution2:
    def trap(self, height):
        stack = []
        i = 0
        ans = 0

        while i < len(height):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0: break
                distance= i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]
                ans += distance * h

            stack.append(i)
            i += 1
        return ans

class Solution3:

    def trap(self, height):
        left = []
        for idx, h in enumerate(height):
            left.append(max(h, left[-1] if len(left) != 0 else float('-inf')))

        right = [0]*len(height)
        for i in range(len(height)-1, -1, -1):
            right[i] = max(height[i], right[i+1] if i+1<len(height) else float('-inf'))

        ans = 0
        for idx, h in enumerate(height):
            ans += min(left[idx], right[idx]) - h

        return ans

if __name__ == '__main__':
    print(Solution3().trap([4, 2, 0, 3, 2, 5]))