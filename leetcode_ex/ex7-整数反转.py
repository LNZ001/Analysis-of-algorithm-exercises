class Solution:
    def reverse(self, x: int) -> int:
        sub = False
        if x < 0:
            sub = True
        k = list(str(abs(x)))
        k.reverse()
        result = int(f"{'-' if sub else ''}{''.join(k)}")
        if -2**31 <= result <= 2**31-1: return result
        return 0



if __name__ == '__main__':
    print(Solution().reverse(-123))