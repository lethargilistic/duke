from duke import Game
from movement import *

class Controller():
    def __init__(self, game):
        self.game = game
        self.set_up_player(1)
        self.set_up_player(2)

    def set_up_player(self, player_number):
        print("Set Up Player", player_number)
        right_or_left_for_duke = input("Place Duke on 1) Right or 2) Left?")
        duke_on_right = None
        if right_or_left_for_duke == "1":
            duke_on_right = True
        elif right_or_left_for_duke == "2":
            duke_on_right = False
        else:
            raise IndexError("Choose right or left")

        footman1_position = int(input("Right to left (1, 2, or 3) where do you want Footman 1? "))
        footman2_position = int(input("Right to left (1, 2, or 3) where do you want Footman 2? "))
        footman_positions = {footman1_position, footman2_position}
        self.game.create_player(player_number, duke_on_right, footman_positions)

    def move_piece(self, player):
        if player not in [1,2]:
            raise IndexError("Player must be 1 or 2")
        pieces = self.game.player_pieces[player]
        piece_list = []
        for num, piece in enumerate(pieces):
            print(str(num) + ":", pieces[piece].whoami())
            piece_list.append(piece)
        piece_choice = int(input("Which piece?"))
        piece_id = piece_list[piece_choice]
        piece_obj = pieces[piece_id]
        valid_moves = self.game.filter_moves(piece_id, piece_obj.move())
        if valid_moves:
            for count, move in enumerate(valid_moves):
                print(count, move)
        else:
            print([])
        choice = valid_moves[int(input("Choose an option"))]
        self.game.move_piece(piece_obj, choice)
        piece_obj.toggle_side()

    def take_turn(self) -> bool:
        print("Player", self.game.current_player)
        player = self.game.current_player
        move_choice = input("1) Move a piece or 2) place a new one")
        if move_choice == "1":
            self.move_piece(player)
        elif move_choice == "2":
            raise NotImplementedError("Can't place pieces yet.")
        else:
            raise IndexError("Choice must be 1 or 2")

        self.game.toggle_player()
        return True
