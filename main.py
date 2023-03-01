import pygame, sys

pygame.init()


FPS = pygame.time.Clock()

W, H = 640, 480


SCREEN = pygame.display.set_mode((W, H))


LUIGI_X , LUIGI_Y = 33, 426
JUMP = LUIGI_Y - 50

SPRITE_X = 8
SPRITE_Y = 401

luigi = pygame.transform.scale(pygame.image.load("luigi.png"), (50, 50))
mysprite = pygame.transform.scale(pygame.image.load("mypixel.png"), (50, 50))

pygame.display.set_caption("the game")

BG_COLOR = (42, 12, 145)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        LUIGI_X -= 1
    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        LUIGI_X += 1
    if keys_pressed[pygame.K_SPACE]:
        LUIGI_Y -= 50 
        
        
        
    print(LUIGI_X, LUIGI_Y)
    print(SPRITE_X, SPRITE_Y)
            
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(luigi, (LUIGI_X, LUIGI_Y))
    SCREEN.blit(mysprite, (SPRITE_X, SPRITE_Y))

    FPS.tick(60)
    pygame.display.update()
    

    