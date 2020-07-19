from typing import List

class Solution:
    def myAtoi(self, str: str) -> int:
        if str is None: return 0
        if len(str) == 0: return 0
        pos = 0
        length = len(str)
        while pos < length:
            if str[pos] != " ": break
            pos += 1
        else:
            return 0

        if not str[pos].isdigit() and str[pos] not in ["+", "-"]: return 0

        pos_right = pos
        if str[pos] in ["+", "-"]:
            pos_right += 1

        while pos_right < length:
            if not str[pos_right].isdigit(): break
            pos_right += 1


        if pos_right - pos == 1 and str[pos] in ["+", "-"]: return 0

        return max(-2**31, min(2**31-1, int(str[pos:pos_right])))

if __name__ == '__main__':
    print(Solution().myAtoi("   -42"))