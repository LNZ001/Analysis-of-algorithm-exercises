from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target: return [left+1, right+1]
            elif cur > target:
                right -= 1
            elif cur < target:
                left += 1

        return False

if __name__ == '__main__':
    print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))