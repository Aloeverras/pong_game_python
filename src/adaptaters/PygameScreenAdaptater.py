import pygame
from dataclasses import dataclass
from domaine.ports.DisplayScreenPongGamePort import DisplayScreenPongGamePort

@dataclass
class PygameScreenAdaptater(DisplayScreenPongGamePort):
    width_screen : int = 800
    height_screen : int = 800
    
    def display_screen_pong_game(self):
        pygame.display.set_mode((self.width_screen, self.height_screen))
    
    @property
    def get_width_screen(self) -> int:
        return self.width_screen
    
    @property
    def get_height_screen(self) -> int:
        return self.height_screen