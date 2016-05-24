from duke import Game

class View():
    def __init__(self, game):
        self.game = game
        self.displayboard = ""
        self.update()
        
    def update(self):
        board = self.game.get_board()

        board_size = self.game.get_board_size()
        self.displayboard = [["  " for x in range(board_size)] for y in range(board_size)]
        
        for y, row in enumerate(self.game.get_board()):
            for x, cell in enumerate(row):
                if isinstance(cell, int):
                    if cell in self.game.get_player1_pieces():
                        self.displayboard[y][x] = str(self.game.get_player1_pieces()[cell])
                    elif cell in self.game.get_player2_pieces():
                        self.displayboard[y][x] = str(self.game.get_player2_pieces()[cell])
                    else:
                        raise TypeError("An id was on the board but not belonging to a player")

    def show_board(self):
        count = self.game.get_board_size() - 1
        for row in self.displayboard[::-1]:
            print(str(count)+"|", end="")
            count-=1
            for slot in row:
                print(slot + "|", end="")
            print()
