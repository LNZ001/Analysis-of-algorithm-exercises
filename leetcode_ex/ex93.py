
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if s == "": return []
        results = []
        ips = []

        def iter_address(ss, offset):

            if offset > 0:
                for i in range(1, 4):
                    if 0 <= int(ss[:i]) <= 255 and len(ss)-i <= offset*3 and len(ss)-i >= offset:
                        if len(ss[:i]) > 1 and ss[0] == "0":
                            continue

                        ips.append(ss[:i])
                        iter_address(ss[i:], offset-1)
                        ips.pop(-1)

            else:
                if 0 <= int(ss) <= 255:
                    if len(ss) > 1 and ss[0] == "0":
                        return
                    ips.append(ss)
                    results.append(".".join(ips))
                    ips.pop(-1)

        iter_address(s, 3)
        return results

if __name__ == '__main__':
    print(Solution().restoreIpAddresses("1111"))