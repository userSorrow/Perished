class Generator:
    
    
    def __init__(self):
        self.progress = 0 # max 100
        self.completed = False

    def increaseProgress(self, amount) -> bool:
        self.progress += amount
        if self.progress >= 100:
            self.completed = True
            
        return self.completed

    def workableSpace(self):
        pass

    def __str__(self) -> str:
        return "G"
    
