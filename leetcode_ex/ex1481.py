
from typing import List
import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # map = defaultdict(int)
        # for a in arr:
        #     map[a] += 1
        map = collections.Counter(arr)
        dif_nums = len(map)

        map_2 = collections.Counter(map.values())

        # map_2 = defaultdict(int)
        # for v in map.values():
        #     map_2[v] += 1

        keys = list(map_2.keys())
        keys.sort()

        for key in keys:
            v = map_2[key]
            n = k // key
            if n < v:
                return dif_nums - n
            else:
                dif_nums -= v
                k -= v * key
        return 0


if __name__ == '__main__':
    print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))