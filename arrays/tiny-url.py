class Codec:
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}
        self.base_url = 'https://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_map:
            # convert to a tinyurl
            short_url = self.base_url + str(len(self.encode_map) + 1)
            # store the tiny url in encoding hashmap
            self.encode_map[longUrl] = short_url
            # store the equivalent long url of tiny one in decoded hashmap
            self.decode_map[short_url] = longUrl

        return self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
