'''
这道题解复杂了, 其实m和n的最长前缀就是[m, n]的.
'''

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if len(bin(m)) != len(bin(n)): return 0
        v1 = bin(m & n)[2:]
        v2 = bin(m | n)[2:]
        if '1' not in v1:
            return 0
        else:
            pos = 0
            while pos < len(v1):
                if v1[pos] == v2[pos]:
                    pos += 1
                else:
                    res = v1[:pos] + "0"*(len(v1) - pos)
                    break
            else:
                res = v1

            return int(res, 2)

if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(1, 1))