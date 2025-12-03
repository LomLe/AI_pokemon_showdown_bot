from typing import Optional


class Stats:
    
    def __init__(
        self, 
        hp: Optional[int] = None, 
        max_hp: Optional[int] = None, 
        attack: Optional[int] = None, 
        defense: Optional[int] = None, 
        special_attack: Optional[int] = None, 
        special_defense: Optional[int] = None, 
        speed: Optional[int] = None
    ) -> None:
        self.hp: Optional[int] = hp
        self.max_hp: Optional[int] = max_hp
        self.attack: Optional[int] = attack
        self.defense: Optional[int] = defense
        self.special_attack: Optional[int] = special_attack
        self.special_defense: Optional[int] = special_defense
        self.speed: Optional[int] = speed
    
    def __repr__(self) -> str:
        return f"Stats(hp={self.hp}, max_hp={self.max_hp}, attack={self.attack}, defense={self.defense}, sp_atk={self.special_attack}, sp_def={self.special_defense}, speed={self.speed})"
    
    def __str__(self) -> str:
        parts = []
        if self.hp is not None and self.max_hp is not None:
            parts.append(f"HP: {self.hp}/{self.max_hp}")
        if self.attack is not None:
            parts.append(f"Atk: {self.attack}")
        if self.defense is not None:
            parts.append(f"Def: {self.defense}")
        if self.special_attack is not None:
            parts.append(f"SpA: {self.special_attack}")
        if self.special_defense is not None:
            parts.append(f"SpD: {self.special_defense}")
        if self.speed is not None:
            parts.append(f"Spe: {self.speed}")
        return ", ".join(parts) if parts else "No stats"

