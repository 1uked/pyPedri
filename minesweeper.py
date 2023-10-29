import random, os, time
import pygame


class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [['Z' for _ in range(width)] for _ in range(height)]
        self.hidden_board = [[' ' for _ in range(width)] for _ in range(height)]
        self.reveal_count = 0
        self.first_move = True
        self.time = time.time()
        self.scoreboard = {}
        self.click_count = 0

    def populate_board(self, first_x, first_y):
        mine_count = 0
        while mine_count < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.hidden_board[y][x] != 'X' and not (abs(y - first_y) <= 1 and abs(x - first_x) <= 1):
                self.hidden_board[y][x] = 'X'
                mine_count += 1
        for y in range(self.height):
            for x in range(self.width):
                if self.hidden_board[y][x] != 'X':
                    self.hidden_board[y][x] = str(self.count_mines(x, y))

    def count_mines(self, x, y):
        mine_count = 0
        for i in range(max(0, y - 1), min(self.height, y + 2)):
            for j in range(max(0, x - 1), min(self.width, x + 2)):
                if self.hidden_board[i][j] == 'X':
                    mine_count += 1
        return mine_count

    def print_board(self):
        print('   ', end='')
        for i in range(self.width):
            print(f'{i} ', end='')
        print('\n   ' + '--' * self.width)
        for i in range(self.height):
            print(f'{i} |', end=' ')
            for j in range(self.width):
                print(self.board[i][j], end=' ')
            print()

    def reveal(self, x, y):
        if self.first_move:
            self.populate_board(x, y)
            self.first_move = False

        if self.hidden_board[y][x] == 'X':
            return False
        elif self.board[y][x] == 'Z':
            self.board[y][x] = self.hidden_board[y][x]
            self.reveal_count += 1
            if self.board[y][x] == '0':
                for i in range(max(0, y - 1), min(self.height, y + 2)):
                    for j in range(max(0, x - 1), min(self.width, x + 2)):
                        if self.board[i][j] == 'Z':
                            self.reveal(j, i)
        return True

    def set_inputs(self, x, y):
        if not self.reveal(x, y):
            self.print_board()
            print('Game over! You hit a mine!')
            return False
        elif self.reveal_count == self.width * self.height - self.mines:
            self.print_board()
            print('Congratulations! You cleared the minefield!')
            return False
        return True
