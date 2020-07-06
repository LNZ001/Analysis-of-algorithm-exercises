from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if right and left:
            return max(n - min(right), max(left))
        elif right:
            return n - min(right)
        elif left:
            return max(left)
        else:
            return 0

