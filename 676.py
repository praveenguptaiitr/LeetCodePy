class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for d in dict:
            self.dict.append(d)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for w in self.dict:
            count =0
            for a,b in zip(w,word):
                if a!=b:
                    count+=1

            if count==1:
                return True

        return False


