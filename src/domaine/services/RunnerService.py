from dataclasses import dataclass
from domaine.ports.RunnerPongGamePort import RunnerPongGamePort

@dataclass
class RunnerService:
    runner : RunnerPongGamePort
    
    @property
    def get_runner_pong_game(self) -> RunnerPongGamePort:
        return self.runner