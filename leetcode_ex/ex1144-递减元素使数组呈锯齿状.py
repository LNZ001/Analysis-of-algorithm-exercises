from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2: return 0

        # ########## 奇/偶数都大 ##########
        count_min = float("inf")
        for init_pos in [0, 1]:
            pos = init_pos
            count = 0
            while pos < length:
                tmp = 0
                if pos-1 >= 0 and nums[pos-1] <= nums[pos]:
                    tmp = max(tmp, nums[pos] - nums[pos-1] + 1)
                if pos+1 < length and nums[pos+1] <= nums[pos]:
                    tmp = max(tmp, nums[pos] - nums[pos+1] + 1)

                count += tmp
                pos += 2

            count_min = min(count_min, count)

        return count_min

if __name__ == '__main__':
    print(Solution().movesToMakeZigzag([9,6,1,6,2]))
