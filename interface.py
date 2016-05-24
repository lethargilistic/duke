from duke import Game
from movement import *

class Controller():
    def __init__(self, game):
        self.game = game

    def make_move(self) -> bool:
        player = self.game.get_current_player()
        move_choice = input("1) Move a piece or 2) place a new one")
        if move_choice == "1":
            if player == 1:
                pieces = self.game.get_player1_pieces()
                piece_list = []
                for num, piece in enumerate(pieces):
                    print(str(num) + ":", pieces[piece].whoami())
                    piece_list.append(piece)
                piece_choice = int(input("Which piece?"))
                piece = pieces[piece_list[piece_choice]]
                print(", ".join(map(str,piece.move())))
                piece.toggle_side()
                print(", ".join(map(str,piece.move())))

            elif player == 2:
                pieces = self.game.get_player2_pieces()
                for num, piece in enumerate(pieces):
                    print(str(num) + ":", pieces[piece].whoami())
            else:
                raise IndexError("Player must be 1 or 2")
        elif move_choice == "2":
            raise NotImplementedError("Can't place pieces yet.")
        else:
            raise IndexError("Choice must be 1 or 2")
        return True
