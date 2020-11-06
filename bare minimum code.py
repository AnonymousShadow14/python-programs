from pygame.locals import *
import pygame
pygame.init()

screen=pygame.display.set_mode((750,750))
pygame.display.set_caption("theatre screen")
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

                 
         
    
   
