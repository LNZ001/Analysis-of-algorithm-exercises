from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # ########## 首先计算从0开始, 油箱最空的值和最后一个出发位置 ##########
        ton_pos = 0
        min_ton = 0
        cur = 0
        for idx, g in enumerate(gas):
            c = cost[idx]
            cur += g - c
            if min_ton > cur:
                min_ton = cur
                ton_pos = idx

        if min_ton >= 0:
            return 0

        # min_ton_2 = 0

        return ton_pos+1 if cur >= 0 else -1




if __name__ == '__main__':
    gas = [2,3,4]
    cost = [3,4,3]
    print(Solution().canCompleteCircuit(gas, cost))