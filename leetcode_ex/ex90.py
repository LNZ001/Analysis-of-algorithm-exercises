import collections
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # 记录数量.
        # map = collections.defaultdict(int)
        # nums_set = set()
        # for n in nums:
        #     map[n] += 1
        #     nums_set.add(n)

        results = []
        nums.sort()

        def subset_loop(offset):
            results.append(nums[:])
            last_k = None
            for idx in range(offset, len(nums)):
                # if map[nums[idx]] == 0:
                #     continue
                if nums[idx] == last_k:
                    continue

                last_k = nums[idx]
                k = nums.pop(idx)
                subset_loop(idx)
                nums.insert(idx, k)

        subset_loop(0)
        return results

if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))