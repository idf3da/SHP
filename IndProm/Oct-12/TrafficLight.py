import pygame

resolution = (640, 420)
BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


class TraficLight():
    def __init__(self):
        self.step = 2
        self.values = ['RED', 'YELLOW', 'GREEN']
        self.value = self.values[self.step]

    def drawLiteralyEverything(self):
        pygame.draw.rect(screen, (60,60,60), pygame.Rect(270, 40, 135, 320)) #Base
        pygame.draw.circle(screen, (0,0,0), (337, 100), 45, 3)
        pygame.draw.circle(screen, (0,0,0), (337, 200), 45, 3)
        pygame.draw.circle(screen, (0,0,0), (337, 300), 45, 3)

        if self.value != "BLUE":
            if self.value == "RED":
                pygame.draw.circle(screen, (255,0,0), (337, 100), 45)
            if self.value == "YELLOW":
                pygame.draw.circle(screen, (255,255,0), (337, 200), 45)
            if self.value == "GREEN":
                pygame.draw.circle(screen, (0,255,0), (337, 300), 45)
            
        else:
            pygame.draw.circle(screen, (0,0,144), (337, 100), 45)
            pygame.draw.circle(screen, (0,0,144), (337, 200), 45)
            pygame.draw.circle(screen, (0,0,144), (337, 300), 45)
    def stepChange(self):
        if self.value == "GREEN":
            self.value = "YELLOW"
            self.step += 1
        elif self.value == "YELLOW":
            if self.step % 2 == 0:
                self.value = "BLUE"
                self.BLUE_COUNTER = 0
            else:
                self.value = "RED"
            self.step += 1
        elif self.value == "BLUE":
            if self.BLUE_COUNTER < 2:
                self.BLUE_COUNTER += 1
            else:
                self.value = "GREEN"
                self.step += 1
        elif self.value == "RED":
            self.value = "GREEN"
            self.step += 1

BOX = TraficLight()
running = True
ticker = 0
while running:
    
    clock.tick(60)
    
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            BOX.stepChange()

    screen.fill((255, 255, 255))

    BOX.drawLiteralyEverything()


    pygame.display.flip()

#Made by defolt_17 aka Ilya D