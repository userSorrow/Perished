from core.pallet import Pallet
from core.wall import Wall
from core.generator import Generator


class Structure:
    def __init__(self) -> None:
        self.L = [
            [Wall(), Pallet(), Wall(), None],
            [Pallet(), None, None, None],
            [Wall(), None, None, None],
            [Generator(), None, None, None]]
        self.shack = [
            [Wall(), Pallet(), Wall(), Wall()],
            [Wall(), None, Generator(), Pallet()],
            [Wall(), None, None, Wall()],
            [Wall(), Wall(), None, Wall()]]
        self.doubleL = [
            [Generator(), Wall(), Pallet(), Wall()],
            [None, None, None, None],
            [Wall(), Pallet(), Wall(), None],
            [None, None, None, None]]