from duke import Game

class View():
    def __init__(self, game):
        self.game = game
        self.displayboard = ""
        self.update()
        
    def update(self):
        board = self.game.board

        board_size = self.game.BOARD_SIZE
        self.displayboard = [["  " for x in range(board_size)] for y in range(board_size)]
        
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if isinstance(cell, int):
                    if cell in self.game.player_pieces[1]:
                        self.displayboard[y][x] = str(self.game.player_pieces[1][cell])
                    elif cell in self.game.player_pieces[2]:
                        self.displayboard[y][x] = str(self.game.player_pieces[2][cell])
                    else:
                        raise TypeError("An id was on the board but not belonging to a player")

    def show_board(self):
        for count, row in enumerate(self.displayboard[::-1]):
            print(str(count)+"|", end="")
            for slot in row:
                print(slot + "|", end="")
            print()
