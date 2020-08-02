
import sys
from functools import lru_cache
class Tang:
    count = 0

    def check(self, tang):
        self.tang = tang
        self.dfs(0)
        return self.count

    # @lru_cache(None)
    def dfs(self, pos):
        if pos == 36:
            self.count += 1
            return
        x = pos // 6
        y = pos % 6

        if self.tang[x][y] == "*":
            self.dfs(pos+1)
        else:
            # 6种植物
            for i in range(6):
                if x-1 < 0 or self.tang[x-1][y] in ["#", "*"] or self.tang[x-1][y] != i:
                    if x + 1 >= 6 or self.tang[x + 1][y] in ["#", "*"] or self.tang[x + 1][y] != i:
                        if y - 1 < 0 or self.tang[x][y - 1] in ["#", "*"] or self.tang[x][y - 1] != i:
                            if y + 1 >= 6 or self.tang[x][y + 1] in ["#", "*"] or self.tang[x][y + 1] != i:
                                self.tang[x][y] = i
                                self.dfs(pos+1)
                                self.tang[x][y] = "#"



if __name__ == '__main__':
    tang = [[]]*6
    for i in range(6):
        tang[i] = list(sys.stdin.readline().strip())
    print(Tang().check(tang))
