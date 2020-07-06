from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        results = []
        stack = [[beginWord]]
        wordSet = set(wordList)
        self.length = 1

        # 每一层
        while True:

            # 一层中的每一次
            s = stack.pop(-1)
            for j in wordSet:

                if self.isConvert():


        dfs(beginWord, endWord)
        return results


    def isConvert(self, word1, word2):
        return sum(True for idx, w in enumerate(word1) if word2[idx] != w) == 1

if __name__ == '__main__':
    print(Solution().findLadders("qa"
,"sq"
,["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))