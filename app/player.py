from typing import List


class Player:
    COLORS = ["red", "yellow", "green", "blue", "magenta"]

    def __init__(self, index: int):
        self.index = index
        self.color = Player.COLORS[index % len(Player.COLORS)]

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.index == other.index

    @property
    def display_name(self) -> str:
        return f"Player {self.index + 1}"

    @property
    def display_color(self) -> str:
        return f"[bold {self.color}]O[/bold {self.color}]"

    @property
    def rich_display_name(self) -> str:
        return f"[bold {self.color}]{self.display_name}[/bold {self.color}]"

    @classmethod
    def create_players(cls, count: int) -> List["Player"]:
        if count < 2 or count > len(cls.COLORS):
            raise ValueError(f"Player count must be between 2 and {len(cls.COLORS)}")
        return [cls(i) for i in range(count)]
