class Premades:
    def __init__(self):
        import builtins, urllib.parse
        self.builtins = builtins
        self.urllib = urllib.parse

    def __str__(self):
        return f"Premade class made by Ferch"

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



premades = Premades()