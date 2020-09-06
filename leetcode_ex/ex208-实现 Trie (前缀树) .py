from typing import List
from collections import defaultdict
from functools import reduce
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: defaultdict(Trie)
        self.trie = Trie()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        reduce(dict.__getitem__, word, self.trie)[True] = word


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_trie = self.trie
        for w in list(str(word)):
            if w in current_trie:
                current_trie = current_trie[w]
            else:
                return False

        return True in current_trie


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # if prefix == "": return True
        current_trie = self.trie
        for w in list(str(prefix)):
            if w not in current_trie: return False
            current_trie = current_trie[w]

        return True

if __name__ == '__main__':
    trie = Trie()
    print(trie.startsWith(""))

