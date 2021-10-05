import pygame

class Bullet:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15

    def draw(self,screen):
        screen.blit(pygame.image.load('images/bullet.png'), (self.x + 17,self.y + 10))