import pygame
import random
import os.path
from classes.Player import Player
from classes.Enemy import Enemy
from classes.Bullet import Bullet
#Initiallize the pygame:
pygame.init()

caption = pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('images/spaceship.png')
bg = pygame.image.load('images/space.jpg')
font = pygame.font.SysFont('comicsans',50,True,True)
score = 0
pygame.display.set_icon(icon)

player = Player(370,480,64,64)
alien = Enemy(random.randint(0,736),random.randint(50,150),64,64,720)
bullets = []
aliens = [alien]
shootLoop = 0

def redraw_game_window():
    screen = pygame.display.set_mode((800, 600))
    screen.blit(bg, (0, -200))
    player.draw(screen)
    for alien in aliens:
        alien.draw(screen)
        alien.move()

    for bullet in bullets:
        bullet.draw(screen)

    text1 = font.render('Score: ' + str(score),1,(0,0,0))
    screen.blit(text1, (550,20))

    pygame.display.update()

#Game loop:
run = True
while run:
    pygame.time.delay(15)
    #Setting all the drawings onto the game
    redraw_game_window()
    #Event set:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Bullet movement:
    for bullet in bullets:
        if bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #Bullet - Enemy collision
    for alien in aliens:
        for bullet in bullets:
            if bullet.y <= alien.hitbox[1] + alien.hitbox[3] and bullet.y >= alien.hitbox[1]:
                if bullet.x <= alien.hitbox[0] + alien.hitbox[2] and bullet.x >= alien.hitbox[0]:
                    bullets.pop(bullets.index(bullet))
                    aliens.pop(aliens.index(alien))
                    score += 1
                    alien = Enemy(random.randint(0,735),random.randint(50,150),64,64,720)
                    aliens.append(alien)

    #Player - Enemy collision
    for alien in aliens:
        if player.hitbox[1] < alien.hitbox[1] + alien.hitbox[3] and alien.hitbox[1] < player.hitbox[1] + player.hitbox[3]:
            if player.hitbox[0] < alien.hitbox[0] and alien.hitbox[0] < player.hitbox[0] + player.hitbox[2]:
                player.hit()
                run = False

    #Keyboard adjustments:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.x += player.vel
        if player.x >= 736:
            player.x = 736

    if keys[pygame.K_LEFT]:
        player.x -= player.vel
        if player.x <= 0:
            player.x = 0

    if keys[pygame.K_SPACE] :
        if len(bullets) < 1:
            bullets.append(Bullet(player.x,player.y,32,32))
        shootLoop = 1

pygame.quit()