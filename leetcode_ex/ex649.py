from typing import List


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        length = len(senate)
        senate_list = senate


        while True:
            r_pop = 0
            d_pop = 0

            for i in range(length):
                if senate_list[i] == None: continue
                if senate_list[i] == "R":
                    r_pop = max(i, r_pop)
                    while True:
                        if senate_list[r_pop] == "D":
                            senate_list[r_pop] = None
                            break
                        r_pop = (r_pop + 1) % length
                        if r_pop == i: return "Radiant"
                        continue
                else:
                    d_pop = max(i, d_pop)
                    while True:
                        if senate_list[d_pop] == "R":
                            senate_list[d_pop] = "0"
                            break
                        d_pop = (d_pop + 1) % length
                        if d_pop == i: return "Dire"
                        continue



if __name__ == '__main__':
    print(Solution().predictPartyVictory("DRRDRDRDRDDRDRDR"))


