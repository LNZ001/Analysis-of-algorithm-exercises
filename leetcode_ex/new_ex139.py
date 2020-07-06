from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def back_track(word):
            if not word:
                return True

            for i in range(0, len(word)):
                if word[i:] in wordDict and back_track(word[:i]):
                    return True
            return False

        return back_track(s)
