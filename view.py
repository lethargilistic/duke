from duke import Game

class View():
    def __init__(self, game):
        self.game = game

    def show_board(self):
        for count, row in enumerate(self.game.board[::-1]):
            print(str(Game.BOARD_SIZE-count-1)+"|", end="")
            for cell in row:
                if isinstance(cell, int):
                    if cell in self.game.player_pieces[1]:
                        print(str(self.game.player_pieces[1][cell]) + "|", end="")
                    elif cell in self.game.player_pieces[2]:
                        print(str(self.game.player_pieces[2][cell]) + "|", end="")
                    else:
                        raise ValueError("An id was on the board but not belonging to a player")
                elif cell == Game.BLANK_TILE:
                    print(cell + "|", end="")
                else:
                    raise ValueError("An unexpected element on the board encountered")
            print()
