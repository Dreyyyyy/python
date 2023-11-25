class console:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def runGame(self, name):
        print(f"{name} is running...")

    def get_name(self):
        print(f"Console name: {self.name}")

    def get_price(self):
        print(f"Console price: {self.price}")

    def get_year(self):
        print(f"Console year: {self.year}")


xbox = console("Xbox", "2020", "$199")

xbox.runGame("Fortnite")

xbox.get_name()
xbox.get_price()
xbox.get_year()


class ps5(console):
    def __init__(self, name, year, price, id):
        super().__init__(name, year, price)
        self.id = id

    def exclusive_games(self, name):
        self.name = name
        print(f"Exclusive game: {self.name}")


ps5 = ps5("PS5", "2019", "399", "2A523M625Z")
ps5.exclusive_games("God of War")

print("\n\n")

for v in (xbox, ps5):
    v.get_name()
    v.get_price()
    v.get_year()
