import pygame, time, random

def rand():
    return random.randint(1, 3)

pygame.init()
resolution = (1440, 900)
dvdLogoSpeed = [rand(), rand()]
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode(resolution)

dvdLogo = pygame.image.load("DVD"+".png")
dvdLogoRect = dvdLogo.get_rect()

def swap_color(dvdLogo):
    return pygame.image.load("DVD"+str(random.randint(1, 7))+".png")

#Fullscreen
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True

dvdLogoRect = dvdLogo.get_rect()

dvdLogoRect[2] -= 12
dvdLogoRect[3] -= 10
dvdLogoRect[0] = random.randint(0, resolution[0] - dvdLogoRect[2])
dvdLogoRect[1] = random.randint(0, resolution[1] - dvdLogoRect[3])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                #Пришлось перезагружаться без этого.
    
    if dvdLogoRect.left <= 0 or dvdLogoRect.right >= resolution[0]:
        dvdLogoSpeed[0] = -rand() if dvdLogoSpeed[0] >= 0 else rand()
        dvdLogo = swap_color(dvdLogo)
    if dvdLogoRect.top <= 0 or dvdLogoRect.bottom >= resolution[1]:
        dvdLogoSpeed[1] = -rand() if dvdLogoSpeed[1] >= 0 else rand()
        dvdLogo = swap_color(dvdLogo)

    screen.fill(backgroundColor)
    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)


    pygame.display.flip()
    time.sleep(1 / 90)
