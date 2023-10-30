import pygame
import button
import display
import time

pygame.init()

#create game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Peridox")

clock = pygame.time.Clock()

running = True

