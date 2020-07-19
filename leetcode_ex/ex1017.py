class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0: return "0"
        bin_list = [0]*2 + list(map(int, bin(N)[2:]))
        length = len(bin_list)

        for idx, b in enumerate(range(length-1, -1, -1)):
            if bin_list[b] == 0:
                continue
            else:
                n = (bin_list[b] + (idx % 2 == 0)) // 2
                v = bin_list[b] % 2
                bin_list[b - 1] += n
                bin_list[b] = v

        result = "".join(map(str, bin_list))
        pos = 0
        while result[pos] == "0" and pos + 1 < length:
            pos += 1
        return result[pos:]


if __name__ == '__main__':
    print(Solution().baseNeg2(3))