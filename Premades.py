class Premades:
    def __init__(self):
        import builtins
        self.builtins = builtins

    def __str__(self):
        return f"Premade class made by Ferch"

    def log(self, content, end="\n", amount=1):
        for _ in range(amount):
            self.builtins.print(content, end=end)




premades = Premades()