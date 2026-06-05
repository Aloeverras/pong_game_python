import pygame
import sys
from domaine.ports.RunnerPongGamePort import RunnerPongGamePort

class PygameRunnerPongGameAdaptater(RunnerPongGamePort):
    
    def start_runner_pong_game(self):
        
        pygame.init()
        
        width = 800
        height = width
        
        white = (255, 255, 255)
        black = (0, 0, 0)
        
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong")
        
        speed_ball_x = 7 * (-1) **(pygame.time.get_ticks() % 2)
        speed_ball_y = 7 * (-1) **(pygame.time.get_ticks() % 2)
        
        palette_speed = 7
        
        ball = pygame.Rect(width // 2 -15, height // 2 -15, 30, 30)
        player1 = pygame.Rect(width - 20, height // 2 - 70, 10, 140)
        player2 = pygame.Rect(10, height // 2 - 70, 10, 140)
        
        scrore_player1 = 0
        scrore_player2 = 0
        police = pygame.font.Font(None, 36)
        
        time = pygame.time.Clock()
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            touche = pygame.key.get_pressed()
            
            if touche[pygame.K_UP] and player1.top > 0:
                player1.y -= palette_speed      
                
            if touche[pygame.K_DOWN] and player1.bottom < height:
                player1.y += palette_speed    
                
            if touche[pygame.K_m] and player2 > 0:
                player2.y -= palette_speed    
                
            if touche[pygame.K_s] and player2.bottom < height:
                player2.y += palette_speed      