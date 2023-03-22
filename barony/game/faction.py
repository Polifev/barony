class Faction:
    name: str
    loyalty: int
    influence: int

    def __init__(self, name, loyalty: int, influence: int):
        self.name = name
        self.loyalty = 10
        self.influence = 10