from typing import Callable

from barony.game.kingdom import Kingdom


class EventChoice:
    def __init__()

class Event:
    can_happen: 'Callable[[Kingdom], bool]'
    name: str
    description: str
    
    # TODO implement choices
    #choices: Dict[]

    def __init__(self, can_happen: 'Callable[[Kingdom], bool]'):
        self.can_happen = can_happen
