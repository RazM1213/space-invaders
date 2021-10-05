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