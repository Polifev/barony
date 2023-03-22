from typing import Dict
from barony.game.faction import Faction


class Kingdom:
    treasury: int
    manpower: int
    faith: int
    legitimacy: int

    factions: Dict[str, Faction]

    def __init__(self):
        self.treasury = 10
        self.manpower = 10
        self.faith = 10
        self.legitimacy = 10

        self.factions = {
            "nobles": Faction("nobles", 40, 60),
            "clercs": Faction("clercs", 30, 40),
            "merchants": Faction("merchants", 10, 10)
        }
