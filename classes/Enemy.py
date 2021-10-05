import pygame

class Enemy:

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.vel = 3
        self.path = [self.x, self.end]
        self.hitbox = (self.x, self.y -8 , 65,70)

    def move(self):
        if self.vel > 0:
            if self.x +self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * (-1)
                self.y += 25

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * (-1)
                self.y += 40


    def draw(self,screen):
        screen.blit(pygame.image.load('images/enemy.png'), (round(self.x),round(self.y)))
        self.hitbox = (self.x, self.y -8 , 65,70 )