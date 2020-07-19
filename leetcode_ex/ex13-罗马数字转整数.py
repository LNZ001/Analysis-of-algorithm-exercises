class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        mapp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        last = None
        for i in range(len(s)-1, -1, -1):
            if last is not None and mapp[s[i]] < last:
                num -= mapp[s[i]]
            else:
                num += mapp[s[i]]
            last = mapp[s[i]]
        return num

if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))

