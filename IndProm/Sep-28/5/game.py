import pygame, time, random

pygame.init()
resolution = (1440, 900) #MBA13
backgroundColor = 0, 0, 0
logos = []
global_speed = (-2, 2)

screen = pygame.display.set_mode(resolution)
pygame.mouse.set_visible(0)

#Fullscreen
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def nonzero_start_speed(global_speed = global_speed):
    a = 0
    while a == 0:
        a = random.randint(global_speed[0], global_speed[1])
    return a

class logo():
    def __init__(self):
        self.speed = [nonzero_start_speed(), nonzero_start_speed()]
        self.img = pygame.image.load("DVD"+str(random.randint(1, 7))+".png")
        self.rect = self.img.get_rect()
        self.rect[2] -= 12
        self.rect[3] -= 10
        self.rect[0] = random.randint(0, resolution[0] - self.rect[2])
        self.rect[1] = random.randint(0, resolution[1] - self.rect[3])
    
    def rand_color(self):
        self.img = pygame.image.load("DVD"+str(random.randint(1, 7))+".png")

running = True

logos.append(logo())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                #Пришлось перезагружаться без этого.
            elif event.key == pygame.K_UP:
                logos.append(logo())
            elif event.key == pygame.K_DOWN:
                logos.pop()                
            elif event.key == pygame.K_RIGHT:
                for i in logos:
                    i.speed[0] += 1
                    i.speed[1] += 1
            elif event.key == pygame.K_LEFT:
                for i in logos:
                    i.speed[0] -= 1
                    i.speed[1] -= 1
    
    for i in logos:
        if i.rect.left <= 0 or i.rect.right >= resolution[0]:
            i.speed[0] = -i.speed[0]
            i.rand_color()
        if i.rect.top <= 0 or i.rect.bottom >= resolution[1]:
            i.speed[1] = -i.speed[1]
            i.rand_color()

    screen.fill(backgroundColor)

    for i in logos:
        screen.blit(i.img, i.rect)
        i.rect = i.rect.move(i.speed)

    pygame.display.flip()
    time.sleep(1 / 120)
