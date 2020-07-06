class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = path.split("/")
        results = []
        for q in queue:
            if q == "":
                continue
            elif q == ".":
                continue
            elif q == "..":
                results.pop(-1)
            else:
                results.append(q)

        return "/" + "/".join(results)

if __name__ == '__main__':
    print(Solution().simplifyPath())
