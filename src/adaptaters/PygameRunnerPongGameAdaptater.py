import pygame
from domaine.ports.RunnerPongGamePort import RunnerPongGamePort

class PygameRunnerPongGameAdaptater(RunnerPongGamePort):
    
    def start_runner_pong_game(self):
        
        pygame.init()
        
        white = (255, 255, 255)
        black = (0, 0, 0)
        
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Pong")
        
        speed_ball_x = 7 * (-1) **(pygame.time.get_ticks() % 2)
        speed_ball_y = 7 * (-1) **(pygame.time.get_ticks() % 2)