class Premades:
    def __init__(self):
        import builtins, urllib.parse, random
        self.builtins = builtins
        self.urllib = urllib.parse
        self.random = random

    def __str__(self):
        return "Premade class made by Ferch"

    def log(self, content, end="\n", amount=1):
        for _ in range(amount):
            self.builtins.print(content, end=end)

    def urllib_quote(self, content, plus=False):
        if plus:
            return self.urllib.quote_plus(content)
        return self.urllib.quote(content)

    def urllib_unquote(self, content, plus=False):
        if plus:
            return self.urllib.unquote_plus(content)
        return self.urllib.unquote(content)

    def randint(self, n1, n2):
        return self.random.randint(n1, n2)

    def forin(self, collection, separator="\n"):
        return separator.join(str(item) for item in collection)

premades = Premades()
