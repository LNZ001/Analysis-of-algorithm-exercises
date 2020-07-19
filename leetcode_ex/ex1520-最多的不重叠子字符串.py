'''
需要记忆的点:
def toNum(self, alpha): return ord(alpha) - ord("a")
def toAscii(self, num): return chr(num + ord("a"))
'''
from typing import List
import copy
from collections import defaultdict, Counter


class Solution:
    def toNum(self, alpha):
        return ord(alpha) - ord('a')

    def toAscii(self, num):
        return chr(num + ord("a"))

    def maxNumOfSubstrings(self, s: str) -> List[str]:
        mapp = {}
        # ########## 记录最新的位置. ##########
        pre = [-1]*26
        for idx, ss in enumerate(s):
            pre[self.toNum(ss)] = idx
            if mapp.get(ss) is None:
                mapp[ss] = [idx, idx, set()]
            else:
                for i in range(26):
                    if mapp[ss][1] < pre[i] < idx and i != self.toNum(ss):
                        mapp[ss][2].add(i)
                mapp[ss][1] = idx

        new_mapp = copy.deepcopy(mapp)
        while True:
            for alpha, mp in mapp.items():
                for i in mp[2]:
                    cur = mapp[self.toAscii(i)]
                    new_mapp[alpha][0] = min(new_mapp[alpha][0], cur[0])
                    new_mapp[alpha][1] = max(new_mapp[alpha][1], cur[1])
            if mapp == new_mapp: break
            mapp = new_mapp

        next_list = list(set({(mp[0], mp[1]) for i, mp in mapp.items()}))
        next_list.sort(key=lambda x: x[0])

        res = []
        for idx, n in enumerate(next_list):
            if idx+1 >= len(next_list) or n[1] < next_list[idx+1][0]:
                res.append(s[n[0]:n[1]+1])

        return res




if __name__ == '__main__':
    print(Solution().maxNumOfSubstrings("ababaf"))
