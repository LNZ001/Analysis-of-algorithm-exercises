class Solution:
    def isHappy(self, n: int) -> bool:
        old = set()
        while n not in old:
            old.add(n)
            res = 0
            for j in map(int, str(n)):
                res += j**2
            if res == 1:
                return True
            n = res
        return False

if __name__ == '__main__':
    print(Solution().isHappy(16))