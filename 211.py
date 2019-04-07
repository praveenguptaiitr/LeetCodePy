class TrieNode:
    def __init__(self):
        self.dict = {}
        self.isEOW = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for i in word:
            if current.dict.get(i,None)==None:
                current.dict[i]=TrieNode()
            else:
                node = current.dict[i]
            current=current.dict[i]
        current.isEOW=True

    def _search(self, word, node):
        curr = node
        for i in word:
            if i == ".":
                if len(curr.dict.keys())==0:
                    return False
                else:
                    ans = False
                    for k in curr.dict.keys():
                        ans = ans or self._search(word[1:],curr.dict[k])
                    return ans
            else:
                if node.dict.get(i, None)==None:
                    return False
                else:
                    return self._search(word[1:],curr.dict[i])
        return node.isEOW


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        current = self.root
        if self._search(word, current)==True:
            return True

        return False


if __name__ == "__main__":
    w = WordDictionary()
    w.addWord("a")
    w.addWord("a")
    print(w.search("."))
    print(w.search("a"))
    print(w.search("aa"))
    print(w.search("a"))
    print(w.search(".a"))
    print(w.search("a."))
    print("Hello")

    '''["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
    [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]'''
    '''[null,null,null,true,true,false,true,false,false]'''

    w = WordDictionary()
    #["WordDictionary", "addWord", "addWord", "addWord", "addWord", "search", "search", "addWord", "search", "search",
    # "search", "search", "search", "search"]
    #[[], ["at"], ["and"], ["an"], ["add"], ["a"], [".at"], ["bat"], [".at"], ["an."], ["a.d."], ["b."], ["a.d"], ["."]]
    # w.addWord("at")
    # w.addWord("and")
    # w.addWord("an")
    # w.addWord("add")
    # print(w.search("a"))
    # print(w.search(".at"))
    # w.addWord("bat")
    # print(w.search(".at"))
