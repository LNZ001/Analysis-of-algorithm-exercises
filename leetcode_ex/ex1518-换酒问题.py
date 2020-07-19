from typing import List

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            key = numBottles // numExchange
            res += key
            numBottles = numBottles % numExchange + key

        return res

if __name__ == '__main__':
    print(Solution().numWaterBottles(2, 3))