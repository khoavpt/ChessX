from abc import abstractmethod
from game import Game

class State: 
    def __init__(self, game: Game) -> None:
        self.game = game


    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    
