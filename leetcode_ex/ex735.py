from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        length = len(asteroids)
        n_list = [None]*length

        last_v = None
        cur = float("-inf")
        for i in range(length):
            if asteroids[i] > 0:
                cur = max(cur, asteroids[i])
            else:
                if last_v is None:
                    if abs(asteroids[i]) > cur:
                        n_list[i] = True
                    else:
                        n_list[i] = cur
                else:
                    if (last_v is True or abs(last_v) < abs(asteroids[i])) and cur < abs(asteroids[i]):
                        n_list[i] = True
                    else:
                        n_list[i] = cur
                last_v = n_list[i]
                cur = float("-inf")

        last_v = None
        cur = None
        for i in range(length-1, -1, -1):
            if asteroids[i] < 0:
                cur = min(cur, asteroids[i]) if cur is not None else asteroids[i]
            else:
                if last_v is None:
                    if cur is None or (asteroids[i]) > abs(cur):
                        n_list[i] = True
                    else:
                        n_list[i] = cur
                else:
                    if (last_v is True or abs(last_v) < abs(asteroids[i])) and (cur is None or (cur) < asteroids[i]):
                        n_list[i] = True
                    else:
                        n_list[i] = cur
                last_v = n_list[i]
                cur = None

        result = []
        for i in range(len(asteroids)):
            if n_list[i] == True:
                result.append(asteroids[i])
        return result

if __name__ == '__main__':
    print(Solution().asteroidCollision([-2, -2, 1, -1]))