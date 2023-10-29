import pygame
import button
import display

pygame.init()

#create game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Peridox")

programIcon = pygame.image.load('Data/icon.png')
bg = pygame.image.load("Data/background.png")
start_btn = pygame.image.load("Data/start_btn.png").convert_alpha()

bg = pygame.transform.scale(bg,(SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_icon(programIcon)

running = True
clock = pygame.time.Clock()

# create window end

# Button Class
start_img = pygame.image.load('Data/start_btn.png').convert_alpha()

#create button instances
start_button = button.Button(400, 300, start_img, 0.8)



# Game Loop

while running:
  screen.blit(bg, (0, 0))

  if start_button.draw(screen):
    display.main()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  pygame.display.flip()
  clock.tick(60)

# Game Loop End

pygame.quit()




