class Solution:

    def compute(self, n, k):
        '''
        第一天吃k块, 至少需要多少块.
        :param k:
        :return:
        '''
        pos = 1
        cur = k
        count = k
        while pos < n:
            if k % 2 ==0:
                cur = cur//2
            else:
                cur = cur//2 + 1
            count += cur
            pos += 1
        return count

    def twosplit(self, n, m):
        '''

        :param n: 天数
        :param m: 巧克力数量
        :return:
        '''

        l = 1
        r = m
        mid = l + (r-l)//2
        while l <= r:
            v = self.compute(n, mid)
            if v == m:
                return mid
            elif v > m:
                r = mid - 1
            else:
                l = mid + 1
            mid = l + (r - l) // 2

        return r



if __name__ == '__main__':
    print(Solution().twosplit(3, 8))