from typing import Optional


class Status:
    
    def __init__(self, name: str, description: Optional[str] = None) -> None:
        self.name: str = name
        self.description: Optional[str] = description
    
    def __repr__(self) -> str:
        return f"Status(name='{self.name}', description='{self.description}')"
    
    def __str__(self) -> str:
        return self.name

