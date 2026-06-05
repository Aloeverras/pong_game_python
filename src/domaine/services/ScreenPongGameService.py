from dataclasses import dataclass
from domaine.ports.DisplayScreenPongGamePort import DisplayScreenPongGamePort
from domaine.ports.RunnerPongGamePort import RunnerPongGamePort

@dataclass
class ScreenPongGameService:
    display_port : DisplayScreenPongGamePort
    runner : RunnerPongGamePort
    
    @property
    def get_display_screen_port_pong_game(self) -> DisplayScreenPongGamePort:
        return self.display_port
    
    @property 
    def get_runner_pong_game(self):
        return self.runner