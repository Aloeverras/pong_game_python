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
                
            ball.x += speed_ball_x
            ball.y += speed_ball_y
            
            if ball.top <= 0 or ball.bottom >= height:
                speed_ball_y *= -1 
                
            if ball.collidedict(player1) or ball.collidedict(player2):
                speed_ball_x *= -1    
                
                
            if ball.left <= 0:
                scrore_player1 += 1
                ball.center = (width // 2, height // 2)  
                speed_ball_x *= -1      
                
            if ball.right <= 0:
                scrore_player2 += 1
                ball.center = (width // 2, height // 2)  
                speed_ball_x *= -1         
                
            screen.fill(black)    
            pygame.draw.rect(screen, white, player1)
            pygame.draw.rect(screen, white, player2)
            pygame.draw.ellipse(screen, white, ball)
            pygame.draw.aaline(screen, white, (width // 2.0), (height // 2.0))
            
            player1_text = police.render(str(scrore_player1), True, white)
            screen.blit(player1_text, (width // 2 + 20, 20))
            
            player2_text = police.render(str(scrore_player2), True, white)
            screen.blit(player1_text, (width // 2 - 50, 20))
            
            pygame.display.flip()
            time.tick(60)