from dataclasses import dataclass

@dataclass
class Player:
    username: str
    highscore: float
    playhours: float
    dateadded: str