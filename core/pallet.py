class Pallet:
    def __init__(self, positionX=None, positionY=None) -> None:
        self.positionX = positionX
        self.positionY = positionY
        

    def __str__(self) -> str:
        return "/"