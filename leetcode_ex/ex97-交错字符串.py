'''
建议方案: BFS, 动态规划.
bfs这里需要习惯用一轮的tmp, 替代queue, 并利用set去重.
'''
from typing import List
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        if len(s3) == 0: return True

        queue = set()
        queue.add((-1, -1, -1))
        while queue:
            tmp = set()
            for i in range(len(queue)):
                left, right, all = queue.pop()
                if all == len(s3) - 1: return True
                if left == len(s1) - 1:
                    if s2[right + 1:] == s3[all + 1:]:
                        return True
                    continue
                if right == len(s2) - 1:
                    if s1[left + 1:] == s3[all + 1:]:
                        return True
                    continue

                if s1[left+1] == s3[all+1]:
                    tmp.add((left+1, right, all+1))
                if s2[right+1] == s3[all+1]:
                    tmp.add((left, right+1, all+1))
            queue = tmp
        return False



if __name__ == '__main__':
    print(Solution().isInterleave("bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"))
