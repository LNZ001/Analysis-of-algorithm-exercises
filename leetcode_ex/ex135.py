from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # ########## 遇到相同重置到1, 连增连减一次递增 ##########

        count = 0
        last = None

        conti_seq = 0
        last_end = None
        current_count = 0

        for rating in ratings:
            if last is None or last == rating:
                last_end = None
                current_count = 1
                conti_seq = 0
            elif rating > last:
                last_end = None
                if conti_seq >= 0:
                    conti_seq += 1
                    current_count = conti_seq + 1
                else:
                    conti_seq = 1
                    current_count = 2
            elif rating < last:
                if conti_seq <= 0:
                    conti_seq -= 1
                    if last_end is not None and abs(conti_seq) + 1 >= last_end:
                        last_end = None
                        conti_seq -= 1
                    current_count = abs(conti_seq) + 1

                else:
                    last_end = current_count
                    current_count = 1
                    conti_seq = 0

            count += current_count
            last = rating

        return count

if __name__ == '__main__':
    tests = [
        # [1, 0, 2],
        # [1,2,2],
        "1 2 3 4 5 3 2 1 2 6 5 4 3 3 2 1 1 3 3 3 4 2".split()
    ]
    for t in tests:
        print(Solution().candy(t))