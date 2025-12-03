from typing import Optional


class Move:
    def __init__(
        self, 
        name: str, 
        type: Optional[str] = None, 
        attack_power: Optional[int] = None, 
        accuracy: Optional[int] = None,
        priority: Optional[int] = None,
        secondary_effect: Optional[str] = None, 
        pp: Optional[int] = None, 
        max_pp: Optional[int] = None
    ) -> None:
        self.name: str = name
        self.type: Optional[str] = type
        self.attack_power: Optional[int] = attack_power
        self.accuracy: Optional[int] = accuracy
        self.priority: Optional[int] = priority
        self.secondary_effect: Optional[str] = secondary_effect
        self.pp: Optional[int] = pp
        self.max_pp: Optional[int] = max_pp
    
    def __repr__(self) -> str:
        return f"Move(name='{self.name}', type='{self.type}', power={self.attack_power}, pp={self.pp}/{self.max_pp})"
    
    def __str__(self) -> str:
        pp_str = f" ({self.pp}/{self.max_pp} PP)" if self.pp is not None and self.max_pp is not None else ""
        return f"{self.name}{pp_str}"

