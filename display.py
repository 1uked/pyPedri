import pygame
import button

pygame.init()

# create game window


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BOARD_WIDTH = 500
BOARD_HEIGHT = 500

TILE_WIDTH = 50
TILE_HEIGHT = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Peridox")

programIcon = pygame.image.load('Data/icon.png')
bg = pygame.image.load("Data/background.png")

# import tiles
tiles = [0] * 9
for i in range(0, 9):
    tiles[i] = pygame.image.load("Data/Tiles/tile_" + str(i) + ".png")
    tiles[i] = pygame.transform.scale(tiles[i],(TILE_WIDTH,TILE_HEIGHT))

tile_bomb = pygame.image.load("Data/Tiles/tile_mine.png")
tile_plain = pygame.image.load("Data/Tiles/tile_plain.png")
tile_wrong = pygame.image.load("Data/Tiles/tile_wrong.png")
tile_flag = pygame.image.load("Data/Tiles/tile_flag.png")

tile_bomb = pygame.transform.scale(tile_bomb,(TILE_WIDTH,TILE_HEIGHT))
tile_plain = pygame.transform.scale(tile_plain,(TILE_WIDTH,TILE_HEIGHT))
tile_wrong = pygame.transform.scale(tile_wrong,(TILE_WIDTH,TILE_HEIGHT))
tile_flag = pygame.transform.scale(tile_flag,(TILE_WIDTH,TILE_HEIGHT))


#mp = pygame.transform.scale(mp, (BOARD_WIDTH, BOARD_HEIGHT))
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_icon(programIcon)

running = True
clock = pygame.time.Clock()

arr = [['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'X', '1', '2', 'Z', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', '3', 'Z'],
       ['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'Z', 'Z', 'Z', '8', 'X', 'Z', 'Z', 'Z', 'Z'],
       ['Z', 'X', 'Z', 'Z', 'Z', 'X', 'Z', 'Z', 'Z', 'Z']]


# create window end

def action(x, y):
    if 150 < x < 650:
        if 50 < y < 550:
            x = (x - 150) // 50
            y = (y - 50) // 50
            print(x,y)


def display(arr):
    for i, _ in enumerate(arr):
        for j, _ in enumerate(arr[i]):
            if arr[i][j] == "Z":
                screen.blit(tile_plain, ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * 50,
                            (SCREEN_HEIGHT - BOARD_HEIGHT) // 2 + j * 50))
            elif arr[i][j] == "X":
                screen.blit(tile_bomb, ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * 50,
                            (SCREEN_HEIGHT - BOARD_HEIGHT) // 2 + j * 50))
            else:
                screen.blit(tiles[int(arr[i][j])], ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * 50,
                                        (SCREEN_HEIGHT - BOARD_HEIGHT) // 2 + j * 50))



# Game Loop

while running:
    screen.blit(bg, (0, 0))
    #screen.blit(mp, ((SCREEN_WIDTH - BOARD_WIDTH) // 2, (SCREEN_HEIGHT - BOARD_HEIGHT) // 2))
    display(arr)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            action(event.pos[0], event.pos[1])

    pygame.display.flip()
    clock.tick(60)

# Game Loop End

pygame.quit()
