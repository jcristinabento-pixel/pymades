import urllib.parse, random

class Premades:
    def __init__(self):
        pass

    def __str__(self):
        return "Premade class made by Ferch"

    def log(self, content, end="\n", amount=1):
        for _ in range(amount):
            print(content, end=end)

    def urlib_quote(self, content, plus=False):
        if plus:
            return self.urllib.quote_plus(content)
        return urllib.parse.quote(content)

    def urllib_unquote(self, content, plus=False):
        if plus:
            return
urllib.parse.unquote_plus(content)
        return urllib.parse.unquote(content)

    def randint(self, n1, n2):
        return random.randint(n1, n2)

    def choice(self, sequence):
        return random.choice(sequence)

    def shuffle(self, lst):
        random.shuffle(lst)
        return lst

    def forprint(self, var):
        count = 0
        for content in var:
            print(content)
            count += 1
        return count

premades = Premades()
