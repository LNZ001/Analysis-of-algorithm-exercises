from typing import List
from collections import Counter

'''
没写完， 后面再测试。
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0: return []
        length = len(words[0])

        # ########## deal words ##########
        mapp = Counter(words)

        pos = 0
        nums = []
        while pos + length <= len(s):
            n = mapp.get(s[pos:pos+length])
            if n is None:
                nums.append(len(words))
            else:
                nums.append(n)
            pos += length

        # ########## 遍历 ##########
        records = [None]*(len(words)+1)
        left = 0
        right = 0
        result = []
        while right <= len(nums)-1:
            if nums[right] == len(words):
                left = right+1
            else:

                if records[nums[right]] is not None:
                    # ########## 被记录过. ##########
                    left = max(left, records[nums[right]]+1)
                records[nums[right]] = right

            if right-left == len(words)-1:
                result.append(left*length)

            right += 1

        return result

if __name__ == '__main__':
    print(Solution().findSubstring("wordgoodgoodgoodbestword",
["word","good","best","good"]))