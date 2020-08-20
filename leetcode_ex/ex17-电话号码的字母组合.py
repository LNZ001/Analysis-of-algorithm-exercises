from typing import List

'''
回溯法更清晰， 并且利用一个index参数，可以不对digits进行多次分割。
'''

class Solution:

    mapp = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str, index=0) -> List[str]:
        if len(digits) - index == 0: return []

        results = self.letterCombinations(digits, index + 1)
        res = []
        if results == []: return list(self.mapp[digits[index]])
        for r in results:
            v = self.mapp[digits[index]]
            for i in range(len(v)):
                res.append(v[i]+r)
        return res

if __name__ == '__main__':
    print(Solution().letterCombinations("23"))