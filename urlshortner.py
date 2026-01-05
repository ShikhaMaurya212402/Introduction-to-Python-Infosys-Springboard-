import string

class URLShortener:
    def __init__(self):
        self.url_to_code = {}   # long URL → short code
        self.code_to_url = {}   # short code → long URL
        self.counter = 1
        self.base62 = string.ascii_letters + string.digits

    def _encode(self, num):
        """Convert number to Base62"""
        code = []
        while num > 0:
            code.append(self.base62[num % 62])
            num //= 62
        return ''.join(code[::-1])

    def shorten(self, long_url):
        # Handle duplicate URLs
        if long_url in self.url_to_code:
            return self.url_to_code[long_url]

        short_code = self._encode(self.counter)
        self.counter += 1

        self.url_to_code[long_url] = short_code
        self.code_to_url[short_code] = long_url

        return short_code

    def expand(self, short_code):
        return self.code_to_url.get(short_code, "URL not found")
shortener = URLShortener()

short_url = shortener.shorten("https://example.com/page/123")
print("Short URL:", short_url)

original = shortener.expand(short_url)
print("Original URL:", original)
