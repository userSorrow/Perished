class Generator:
    all = []
    
    def __init__(self, positionX, positionY):
        self.positionX = positionX # added generator position (x, y)
        self.positionY = positionY
        self.progress = 0 # max 100
        self.completed = False
        self.all.append(self)
        

    def increaseProgress(self, amount) -> None:
        self.progress += amount
        if self.progress >= 100:
            self.completed = True
           
    
    def isGenCompleted(self) -> bool:
        return self.completed

    def workableSpace(self):
        pass

    def __str__(self) -> str:
        return "G"
    
