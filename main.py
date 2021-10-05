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
