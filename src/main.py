from domaine.services.RunnerService import RunnerService
from adaptaters.PygameRunnerPongGameAdaptater import PygameRunnerPongGameAdaptater


pong_game = PygameRunnerPongGameAdaptater()
run_service = RunnerService(runner=pong_game)
        
print(" --- start game --- ")
        
run_service.start()      
