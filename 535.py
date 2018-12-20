import string
import random
class Codec:
    def __init__(self):
        self.url2s = {}
        self.s2url = {}
        self.str = string.ascii_letters + '0123456789'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2s:

            x = "".join(random.sample(self.str,6))
            while x in self.s2url:
                x = "".join(random.sample(self.str, 6))

            self.url2s[longUrl]=x
            self.s2url[x]=longUrl
            return x

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.s2url[shortUrl]

# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"

codec = Codec()
codec.decode(codec.encode(url))