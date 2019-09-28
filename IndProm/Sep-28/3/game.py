import pygame
import sys

size = width, height = 800, 600
black = 0, 0, 0
image = pygame.image.load("DVD.png")
imagerect = image.get_rect()

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        screen.fill(black)

        screen.blit(image, imagerect)

        pygame.display.flip()
    sys.exit()
    
main()