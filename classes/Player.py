import pygame

class Player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 20
        self.hitbox = (self.x - 20, self.y -20, 150, 150)

    def hit(self):
        text2 = pygame.font.SysFont('comicsans',150, True,True).render('GAME OVER!', 1, (0,0,0))
        pygame.display.set_mode((800,600)).blit(text2, (10,250))
        pygame.display.update()
        pygame.time.delay(1000)


    def draw(self,screen):
        screen.blit(pygame.image.load('images/character.png'), (round(self.x),round(self.y)))
        self.hitbox = (self.x , self.y , 64,64)
