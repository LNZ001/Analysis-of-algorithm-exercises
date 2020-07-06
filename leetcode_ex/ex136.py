from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numberSet = set()
        for n in nums:
            if n in numberSet:
                numberSet.discard(n)
            else:
                numberSet.add(n)

        return numberSet.pop()

if __name__ == '__main__':
    print(Solution().singleNumber([2, 2,1]))