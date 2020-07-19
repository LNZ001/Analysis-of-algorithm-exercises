from typing import List
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        exists = [False]*256
        left = 0
        right = 0

        max_length = 0
        while right < len(s):
            while exists[ord(s[right])] and left < right:
                exists[ord(s[left])] = False
                left += 1
            max_length = max(max_length, right - left + 1)
            exists[ord(s[right])] = True
            right += 1

        return max_length
if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("dvdf"))