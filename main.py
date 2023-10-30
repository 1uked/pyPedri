import pygame
import button
import display

from tqdm import tqdm, trange
import time

pygame.init()

#create game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Peridox")

programIcon = pygame.image.load('Data/icon.png')
bg = pygame.image.load("Data/bg3T.png")

bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_icon(programIcon)

running = True
clock = pygame.time.Clock()

# create window end

# Button Class
start_img = pygame.image.load('Data/str_btn.png').convert_alpha()
#create button instances
start_button = button.Button(400, 250, start_img, 0.28)

def load(screen):
  WIDTH = 20
  pygame.draw.rect(screen, "black", pygame.Rect(400-WIDTH*5, 500, 200, 30), 5)
  for i in trange(WIDTH):
    time.sleep(0.1)
    pygame.draw.rect(screen, "black", pygame.Rect(400-5*i, 500, 10*i, 30))
    pygame.display.flip()
  pygame.mouse.set_pos(10, 10)

# Game Loop

while running:
  screen.blit(bg, (0, 0))

  if start_button.draw(screen):
    load(screen)
    display.main()
    running = False

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()
  clock.tick(60)

# Game Loop End

pygame.quit()




