from typing import Optional


class Ability:
    
    def __init__(self, name: str, description: Optional[str] = None) -> None:
        self.name: str = name
        self.description: Optional[str] = description
    
    def __repr__(self) -> str:
        return f"Ability(name='{self.name}', description='{self.description}')"
    
    def __str__(self) -> str:
        return self.name

