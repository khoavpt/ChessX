from abc import abstractmethod

class State: 
    def __init__(self, window) -> None:
        self.window = window


    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass
