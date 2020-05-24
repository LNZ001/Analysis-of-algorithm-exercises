class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        aei = "aeiou"
        if not s:
            return 0
        res = ""
        for i in s:
            if i in aei:
                res += "1"
            else:
                res += "0"


        current_count = res[:k].count("1")
        if len(res) <= k:
            return res.count("1")


        queue_list = ""
        max_count = current_count
        for idx, r in enumerate(res):
            if res[idx+k:idx+k+1] == "1":
                current_count += 1
            if r == "1":
                current_count -= 1


            if current_count > max_count:
                max_count = current_count

        return max_count