class Codec:
    def __init__(self):
        from collections import defaultdict
        self.map = defaultdict(str)
        self.mapping = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        import random
        res = ""
        for i in range(6):
            idx = random.randint(0, len(self.mapping)-1)
            res += self.mapping[idx]
        url = 'http://tinyurl.com/' + res
        if not self.map[url]:
            self.map[url] = longUrl
        return url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl]

print(Codec().encode("https://leetcode.com/problems/design-tinyurl"))