import pygame
from integration import *
from game import Game
from colors import Colors

import os, sys
from fcntl import ioctl

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934


pygame.init()
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Pontuação", True, Colors.white)
next_surface = title_font.render("Seguinte", True, Colors.white )
game_over_surface = title_font.render("Fim de Jogo", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen =pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

Integration=IO()
flag=0
flag2=1
numero = "0000"

GAME_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
    for event in pygame.event.get():
	
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if game.game_over == True and Integration.get_SW(0) == 1 and flag==0:
                game.game_over = False
                game.reset()
                flag=1
        if Integration.get_SW(0) == 0:
        		flag=0
        if Integration.get_PB(2)==0 and game.game_over == False:
            game.move_left()
        if Integration.get_PB(0)==0 and game.game_over == False:
            game.move_right()
        if Integration.get_PB(3)==0 and game.game_over == False:
            game.rotate()
        if Integration.get_PB(1)==0 and game.game_over == False:
            game.move_down()
            game.update_score(0, 1)
        numero=str(game.score)
        if game.score >= 0:
        	numero=numero.zfill(4)
        Integration.put_DP(0,numero)
        

        if event.type == pygame.KEYDOWN:
            if game.game_over == True and event.key == pygame.K_k:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()            

    #Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.light_purple)
    
    screen.blit(score_surface,(333, 20, 50, 50))
    screen.blit(next_surface, (345, 180, 50, 50))
    
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.pink, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.pink, next_rect, 0, 10)
    game.draw(screen)
    

    pygame.display.update()
    clock.tick(60)
