import builtins, urllib.parse, random

class Premades:
    def __init__(self):
        self.builtins = builtins
        self.urllib = urllib.parse
        self.random = random

    def __str__(self):
        return "Premade class made by Ferch"

    def log(self, content, end="\n", amount=1):
        for _ in range(amount):
            self.builtins.print(content, end=end)

    def urlib_quote(self, content, plus=False):
        if plus:
            return self.urllib.quote_plus(content)
        return self.urllib.quote(content)

    def urllib_unquote(self, content, plus=False):
        if plus:
            return self.urllib.unquote_plus(content)
        return self.urllib.unquote(content)

    def randint(self, n1, n2):
        return self.random.randint(n1, n2)

    def forprint(self, var):
        count = 0
        for content in var:
            self.builtins.print(content)
            count += 1
        return count

premades = Premades()