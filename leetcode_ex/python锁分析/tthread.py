from typing import List
from threading import Thread
import pprint
from multiprocessing import Lock

class Solution:

    def __init__(self):
        self.n = 100000
        self.result = []

    def check1(self):
        for i in range(self.n):
            self.result.append((1,i))

    def check2(self):
        for i in range(self.n):
            self.result.append((2,i))


if __name__ == '__main__':
    s = Solution()
    t1 = Thread(target=s.check1)
    t2 = Thread(target=s.check2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pprint.pprint(s.result)
