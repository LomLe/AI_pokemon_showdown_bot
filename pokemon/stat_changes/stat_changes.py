class StatChanges:
    
    def __init__(
        self, 
        attack: int = 0, 
        defense: int = 0, 
        special_attack: int = 0, 
        special_defense: int = 0, 
        speed: int = 0
    ) -> None:
        self.attack: int = attack
        self.defense: int = defense
        self.special_attack: int = special_attack
        self.special_defense: int = special_defense
        self.speed: int = speed
    
    def __repr__(self) -> str:
        return f"StatChanges(attack={self.attack}, defense={self.defense}, sp_atk={self.special_attack}, sp_def={self.special_defense}, speed={self.speed})"
    
    def __str__(self) -> str:
        parts = []
        if self.attack != 0:
            parts.append(f"Atk: {self.attack:+d}")
        if self.defense != 0:
            parts.append(f"Def: {self.defense:+d}")
        if self.special_attack != 0:
            parts.append(f"SpA: {self.special_attack:+d}")
        if self.special_defense != 0:
            parts.append(f"SpD: {self.special_defense:+d}")
        if self.speed != 0:
            parts.append(f"Spe: {self.speed:+d}")
        return ", ".join(parts) if parts else "No stat changes"

