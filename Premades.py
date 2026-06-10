import urllib.parse
import random
import time

class Premades:
    def __init__(self):
        self._timers = {}

    def __str__(self):
        return "Premade class made by Ferch"

    def log(self, content, end="\n", amount=1):
        for _ in range(amount):
            print(content, end=end)

    def urllib_quote(self, content, plus=False):
        if plus:
            return urllib.parse.quote_plus(content)
        return urllib.parse.quote(content)

    def urllib_unquote(self, content, plus=False):
        if plus:
            return urllib.parse.unquote_plus(content)
        return urllib.parse.unquote(content)

    def randint(self, n1, n2):
        return random.randint(n1, n2)

    def choice(self, sequence):
        return random.choice(sequence)

    def shuffle(self, sequence):
        random.shuffle(sequence)
        return sequence

    def forprint(self, var):
        count = 0
        for content in var:
            print(content)
            count += 1
        return count

    def timer_start(self, name="default"):
        self._timers[name] = time.perf_counter()

    def timer_end(self, name="default"):
        if name not in self._timers:
            raise ValueError(f"Timer '{name}' not found")
        return time.perf_counter() - self._timers.pop(name)

premades = Premades()