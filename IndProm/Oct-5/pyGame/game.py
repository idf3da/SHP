import pygame

class Player():
    def __init__(self):
        self.rect = pygame.Rect(64, 64, 32, 32)
    def move(self, dx, dy):
        if dx != 0:
            self.move_single(dx, 0)
        if dy != 0:
            self.move_single(0, dy)
    def move_single(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

resolution = (640, 420)
speedo = 3

pygame.init()
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()
player = Player()

running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move(-speedo, 0)
    if key[pygame.K_d]:
        player.move(speedo, 0)
    if key[pygame.K_w]:
        player.move(0, -speedo)
    if key[pygame.K_s]:
        player.move(0, speedo)
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()