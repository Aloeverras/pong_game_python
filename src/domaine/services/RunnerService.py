from dataclasses import dataclass
from domaine.ports.RunnerPongGamePort import RunnerPongGamePort

@dataclass
class RunnerService:
    runner : RunnerPongGamePort
    
    def start(self):
        try:
            self.runner.start_runner_pong_game()
        except Exception as e:
            print(e) 
            print(e.__cause__)   
    
    @property
    def get_runner_pong_game(self) -> RunnerPongGamePort:
        return self.runner