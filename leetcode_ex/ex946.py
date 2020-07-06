from typing import List
from functools import reduce

class Test:
    pass

class Solution(Test):
    def isLast(self, i, j, pushed):
        cur = j
        while cur != i:
            if pushed[cur] != -1 or cur == 0:
                return False
            cur -= 1
        return True

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0:
            return True
        if len(popped) == 0:
            return False
        last_pos = float("-inf")
        # ########## 在弹出之前的所有没有处理的都是倒序的 ##########
        for p in popped:

            pos = pushed.index(p)
            if pos <= last_pos and not self.isLast(pos, last_pos, pushed):
                return False
            pushed[pos] = -1
            last_pos = pos

        return reduce(lambda x, y: x&y, {p == -1 for p in pushed})





if __name__ == '__main__':
    print(Solution().validateStackSequences([1, 0, 2], [2, 1, 0]))