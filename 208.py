class TrieNode:
    def __init__(self):
        self.dict = {}
        self.isEOW = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for i in word:
            node = current.dict.get(i, None)
            if node is None:
                current.dict[i]= TrieNode()
            current = current.dict[i]

        current.isEOW = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in word:
            if current.dict.get(i,None)==None:
                return False
            current = current.dict[i]

        if current.isEOW==True:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for i in prefix:
            if current.dict.get(i,None)==None:
                return False
            current = current.dict[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    t = Trie()
    t.insert("abcde")
    t.insert("abc")
    print("Hello")
