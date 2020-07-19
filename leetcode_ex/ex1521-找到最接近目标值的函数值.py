from typing import List
from functools import reduce

def t(arr, l, r):
    if (r<l):
        return -100000000

    ans = arr[l]
    for i in range(l+1, r+1):
        ans = ans & arr[i]

    return ans

class Solution:

    def toNum(self, counts, length):
        num = 0
        for i in range(len(counts)-1, -1, -1):
            num = num * 2 + (1 if counts[i] == length else 0)
        return num


    def closestToTarget(self, arr: List[int], target: int) -> int:
        left = 0
        right = 0
        counts = [0] * 20

        # if reduce(lambda x, y: x&y, arr[left: right])
        min_max = float("-inf") # 略小
        max_min = float("inf") # 略大
        isUpate = False
        while left <= right:
            while right < len(arr):
                # ########## 右指针向右移动. ##########
                if not isUpate:
                    for idx, i in enumerate(bin(arr[right])[:1:-1]):
                        if i == "1":
                            counts[idx] += 1
                else:
                    isUpate = False

                num = self.toNum(counts, right-left+1)
                if target == num: return 0
                elif target > num:
                    min_max = max(min_max, num)
                    break
                else:
                    max_min = min(max_min, num)
                    right += 1
            else:
                return min(abs(target - min_max), abs(target - max_min))
            # ########## left处理 ##########
            for idx, i in enumerate(bin(arr[left])[:1:-1]):
                if i == "1":
                    counts[idx] -= 1

            left += 1
            if left > right:
                right += 1
            else:
                isUpate = True

        return min(abs(target - min_max), abs(target - max_min))

if __name__ == '__main__':
    print(Solution().closestToTarget([9,12,3,7,15],
5))
