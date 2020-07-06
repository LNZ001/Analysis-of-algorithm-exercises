from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        last = None
        k = None
        for a in arr:
            if last is None:
                pass

            elif k is None:
                k = a - last
            else:
                if a - last == k:
                    pass
                else:
                    return False

            last = a
        return True

if __name__ == '__main__':
    print(Solution().canMakeArithmeticProgression(
[-68,-96,-12,-40,16]))
