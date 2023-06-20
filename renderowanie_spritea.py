import pygame,sys
from pygame.locals import *
from consts import *
from emergency_stop import Emergency_Stop

TITLE = "Smooth Movement"

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x,y,32,32)
        self.x = int(x)
        self.y = int(y)
        self.color = (250,120,60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    def draw(self,win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(self.x, self.y, 32, 32)

player = Player(displaywymiary/2, displaywymiary/2)

def imgtosprite(photo):
        img = pygame.image.load(photo).convert()
        img.set_colorkey((0,0,0))
        img = pygame.transform.scale(img, blockwymiary)

        return img
    
sprite = imgtosprite('./imgs/spritetest.png')

def Sprite_Movement():
    sprite_running = True
    while sprite_running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = True
                if event.key == pygame.K_UP:
                    player.up_pressed = True
                if event.key == pygame.K_DOWN:
                    player.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    player.right_pressed = False
                if event.key == pygame.K_UP:
                    player.up_pressed = False
                if event.key == pygame.K_DOWN:
                    player.down_pressed = False

        .fill((0,0,0))
        player.draw(screen)
        player.update()
        pygame.display.flip()
        clock.tick(120)
        # Emergency_Stop()
        # return
