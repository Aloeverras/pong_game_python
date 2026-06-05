from abc import ABC, abstractmethod

class DisplayScreenPongGamePort(ABC):
    
    @abstractmethod
    def display_screen_pong_game(self):
        pass