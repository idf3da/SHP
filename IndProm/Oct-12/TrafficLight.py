#COPYRIGHT PROTECTION
import pygame #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D

resolution = (640, 420) #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
BLACK = (0, 0, 0) #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
pygame.init() #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
screen = pygame.display.set_mode(resolution) #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
clock = pygame.time.Clock() #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D

#Made by defolt_17 aka Ilya D
class TraficLight(): #Made by defolt_17 aka Ilya D
    #Made by defolt_17 aka Ilya D
    def __init__(self): #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        self.step = 2 #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        self.values = ['RED', 'YELLOW', 'GREEN'] #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        self.value = self.values[self.step] #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D

    def drawLiteralyEverything(self): #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        pygame.draw.rect(screen, (60,60,60), pygame.Rect(270, 40, 135, 320)) #Base #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        pygame.draw.circle(screen, (0,0,0), (337, 100), 45, 3) #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        pygame.draw.circle(screen, (0,0,0), (337, 200), 45, 3) #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        pygame.draw.circle(screen, (0,0,0), (337, 300), 45, 3) #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D

        if self.value != "BLUE": #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            if self.value == "RED": #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                pygame.draw.circle(screen, (255,0,0), (337, 100), 45) #Made by defolt_17 aka Ilya D #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
            if self.value == "YELLOW": #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                pygame.draw.circle(screen, (255,255,0), (337, 200), 45) #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
            if self.value == "GREEN": #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                pygame.draw.circle(screen, (0,255,0), (337, 300), 45) #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
            
        else:
            #Made by defolt_17 aka Ilya D
            pygame.draw.circle(screen, (0,0,144), (337, 100), 45) #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            pygame.draw.circle(screen, (0,0,144), (337, 200), 45) #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            pygame.draw.circle(screen, (0,0,144), (337, 300), 45) #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
    def stepChange(self): #Made by defolt_17 aka Ilya D
        #Made by defolt_17 aka Ilya D
        if self.value == "GREEN":
            #Made by defolt_17 aka Ilya D
            self.value = "YELLOW"
            #Made by defolt_17 aka Ilya D
            self.step += 1
            #Made by defolt_17 aka Ilya D
        elif self.value == "YELLOW": #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            if self.step % 2 == 0: #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                self.value = "BLUE" #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                self.BLUE_COUNTER = 0 #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
            else: #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                self.value = "RED" #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
            self.step += 1 #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
        elif self.value == "BLUE": #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            if self.BLUE_COUNTER < 2: #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                self.BLUE_COUNTER += 1 #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
            else:
                #Made by defolt_17 aka Ilya D
                self.value = "GREEN" #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
                self.step += 1 #Made by defolt_17 aka Ilya D
                #Made by defolt_17 aka Ilya D
        elif self.value == "RED": #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            self.value = "GREEN" #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            self.step += 1 #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D

BOX = TraficLight() #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
running = True #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
ticker = 0 #Made by defolt_17 aka Ilya D
#Made by defolt_17 aka Ilya D
while running:
    #Made by defolt_17 aka Ilya D
    
    clock.tick(60)  #Made by defolt_17 aka Ilya D
    #Made by defolt_17 aka Ilya D
    
    
    for e in pygame.event.get():
        #Made by defolt_17 aka Ilya D
        if e.type == pygame.QUIT:
            #Made by defolt_17 aka Ilya D
            running = False
            #Made by defolt_17 aka Ilya D
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE: #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            running = False #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE: #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D
            BOX.stepChange() #Made by defolt_17 aka Ilya D
            #Made by defolt_17 aka Ilya D

    screen.fill((255, 255, 255)) #Made by defolt_17 aka Ilya D
    #Made by defolt_17 aka Ilya D

    #Made by defolt_17 aka Ilya D
    BOX.drawLiteralyEverything() #Made by defolt_17 aka Ilya D
    #Made by defolt_17 aka Ilya D


    pygame.display.flip() #Made by defolt_17 aka Ilya D 
    #Made by defolt_17 aka Ilya D