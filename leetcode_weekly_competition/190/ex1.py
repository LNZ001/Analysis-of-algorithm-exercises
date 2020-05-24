class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen_list = sentence.split(" ")
        word_len = len(searchWord)
        for idx, s in enumerate(sen_list):

            if s[:word_len] == searchWord:
                return idx + 1
        else:
            return -1