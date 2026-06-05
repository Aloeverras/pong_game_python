from dataclasses import dataclass
from domaine.ports.DisplayScreenPongGamePort import DisplayScreenPongGamePort

@dataclass
class ScreenPongGameService:
    display_port : DisplayScreenPongGamePort
    
    @property
    def get_display_screen_port_pong_game(self) -> DisplayScreenPongGamePort:
        return self.display_port