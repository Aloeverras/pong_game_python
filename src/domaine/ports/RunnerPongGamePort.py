from abc import ABC, abstractmethod


class RunnerPongGamePort(ABC):
    
    @abstractmethod
    def start_runner_pong_game(self):
        pass