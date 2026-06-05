import pygame
import sys
from domaine.ports.RunnerPongGamePort import RunnerPongGamePort
from typing import override

class PygameRunnerPongGameAdaptater(RunnerPongGamePort):
    
    @override
    def start_runner_pong_game(self):
        
        pygame.init()
        
        width = 800
        height = 800
        
        white = (255, 255, 255)
        black = (0, 0, 0)
        
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong")
        
        speed_ball_x = 7 * (-1) ** (pygame.time.get_ticks() % 2)
        speed_ball_y = 7 * (-1) ** (pygame.time.get_ticks() % 2)
        
        palette_speed = 7
        
        ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)
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
            
            # Contrôles Joueur 1 (Droite)
            if touche[pygame.K_UP] and player1.top > 0:
                player1.y -= palette_speed      
                
            if touche[pygame.K_DOWN] and player1.bottom < height:
                player1.y += palette_speed    
                
            # Contrôles Joueur 2 (Gauche)
            if touche[pygame.K_m] and player2.top > 0:
                player2.y -= palette_speed    
                
            if touche[pygame.K_s] and player2.bottom < height:
                player2.y += palette_speed  
                
            # Mouvement de la balle
            ball.x += speed_ball_x
            ball.y += speed_ball_y
            
            # Rebond Haut / Bas
            if ball.top <= 0 or ball.bottom >= height:
                speed_ball_y *= -1 
                
            # Rebond sur les joueurs (Correction collidedict -> colliderect)
            if ball.colliderect(player1) or ball.colliderect(player2):
                speed_ball_x *= -1    
                
            # Score Joueur 2 (Balle sort à gauche)
            if ball.left <= 0:
                scrore_player2 += 1
                ball.center = (width // 2, height // 2)  
                speed_ball_x *= -1      
                
            # Score Joueur 1 (Balle sort à droite)
            if ball.right >= width:
                scrore_player1 += 1
                ball.center = (width // 2, height // 2)  
                speed_ball_x *= -1         
                
            # Dessin des éléments
            screen.fill(black)    
            pygame.draw.rect(screen, white, player1)
            pygame.draw.rect(screen, white, player2)
            pygame.draw.ellipse(screen, white, ball)
            pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))
            
            # Affichage des scores
            player1_text = police.render(str(scrore_player1), True, white)
            screen.blit(player1_text, (width // 2 + 50, 20))
            
            player2_text = police.render(str(scrore_player2), True, white)
            screen.blit(player2_text, (width // 2 - 70, 20))
            
            pygame.display.flip()
            time.tick(60)