import pygame, keyboard as key
from random import randint


# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (63, 153, 192)
WIDTH = 500
HEIGHT = 500
col =(255, 255, 255)
colo = (250, 0, 12)
floor_col = (78, 209, 33)
score = 0
h = open("test.txt", "r")
hscore = h.read()
high = int(hscore.strip())


# Object classes
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        #defines how sprite looks
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        #generates sprite
        pygame.draw.rect(self.image,
                         color,
                         pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

        

#initializes game
pygame.init()

#creates screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("happy geese")



imp = pygame.image.load("E:\\flpappy bridf\\goose2.png").convert()


#--------sprite--------
#creates sprite list
all_sprites_list = pygame.sprite.Group()

#creates player sprite and adds it to sprite list
player = Sprite(col, 20, 30)
player.rect.x = 200
player.rect.y = 250
all_sprites_list.add(player)

#creates pillar sprite and add it to list

pillar_top = Sprite(colo, 250, 40)
pillar_bottom = Sprite(colo, 250, 40)
pillar_top.rect.x = 450
pillar_top.rect.y = -100
pillar_bottom.rect.x = 450
pillar_bottom.rect.y = 320
all_sprites_list.add(pillar_top)
all_sprites_list.add(pillar_bottom)

#creates floor sprite and add it to the list
floor = Sprite(floor_col, 50, 500)
floor.rect.x = 0
floor.rect.y = 450
all_sprites_list.add(floor)

#initializes game
exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        #quits
        if event.type == pygame.QUIT:
            exit = False

    #updates sprites etcw
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    #pillar moving
    if player.rect.y:
        if score >= 80:
            pillar_top.rect.x -= 10
            pillar_bottom.rect.x -= 10
        else:
            pillar_top.rect.x -= (2 + (score/10))
            pillar_bottom.rect.x -= (2 + (score/10))

    #detects when pillar hits wall, and regenerates it
    if pillar_top.rect.x <= -20:
        pillar_top.rect.x = 450
        pillar_top.rect.y = randint(-200, -10)
        pillar_bottom.rect.x = 450
        pillar_bottom.rect.y = pillar_top.rect.y + 400
        score += 1
        print(score)
        
        #sets the highscore for the game
        if score > high:
            with open("test.txt", "w") as f:
                f.write(str(score))
                highs = score
                    
        #detects sprite colision
    collision1 = pygame.sprite.collide_mask(player, pillar_top)
    collision2 = pygame.sprite.collide_mask(player, pillar_bottom)
    collision3 = pygame.sprite.collide_mask(player, floor)
    if collision1 or collision2 or collision3:
        print("Collision")
        if score > high:
            print("the high score is", score)
        else:
            print("the high score is still", high)
        
        exit = False

    #player movement
    if key.is_pressed('w') and player.rect.y >= 50 :
        player.rect.y -= 10

    #gravity
    if player.rect.y <= 450:
        player.rect.y += 5


pygame.quit()
