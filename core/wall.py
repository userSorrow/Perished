class Wall:
    position = []
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.position.append((self.x, self.y))
    
    def __str__(self) -> str:
        return "#"