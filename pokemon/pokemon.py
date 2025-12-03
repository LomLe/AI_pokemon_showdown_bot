from typing import Optional, List

from .stats import Stats
from .ability import Ability
from .item import Item
from .move import Move
from .status import Status
from .stat_changes import StatChanges


class Pokemon:
    def __init__(
        self, 
        name: str, 
        index: Optional[str] = None, 
        active: bool = False, 
        alive: bool = True, 
        level: Optional[int] = None, 
        gender: Optional[str] = None, 
        stats: Optional[Stats] = None, 
        moves: Optional[List[Move]] = None, 
        status: Optional[Status] = None, 
        ability: Optional[Ability] = None, 
        item: Optional[Item] = None,
        stat_changes: Optional[StatChanges] = None
    ) -> None:
        self.name: str = name
        self.index: Optional[str] = index
        self.active: bool = active
        self.alive: bool = alive
        self.level: Optional[int] = level
        self.gender: Optional[str] = gender
        self.stats: Optional[Stats] = stats
        self.moves: List[Move] = moves if moves is not None else []
        self.status: Optional[Status] = status
        self.ability: Optional[Ability] = ability
        self.item: Optional[Item] = item
        self.stat_changes: Optional[StatChanges] = stat_changes
    
    def __repr__(self) -> str:
        active_str = " (ACTIVE)" if self.active else ""
        return f"Pokemon(name='{self.name}', index={self.index}{active_str})"
    
    def __str__(self) -> str:
        return self.name

