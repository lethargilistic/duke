from duke import Game
from view import View
from movement import *

class Controller():
    def __init__(self, game, view):
        self.game = game
        self.view = view
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

    def game_loop(self):
        winner = 0
        self.view.show_board()
        while winner == 0:
            winner = self.take_turn()
            self.view.show_board()
        
        print("Player", winner, "wins!")
        play_again = input("Play again? (y/n)")
        if play_again == y:
            return True
        else:
            return False

    def take_turn(self) -> int:
        print("Player", self.game.current_player)
        player = self.game.current_player
        move_choice = input("1) Move a piece or 2) place a new one ")
        if move_choice == "1":
            self.move_piece(player)
        elif move_choice == "2":
            if not self.game.player_pieces[player]: #no more pieces
                print("Your bag is empty. Choose a piece to move.")
                self.move_piece(player)
            self.place_piece_from_bag(player)
        else:
            raise IndexError("Choice must be 1 or 2")

        self.game.toggle_player()

        # Return winner, or 0 for neither
        if not self.game.has_duke(1):
            return 2
        elif not self.game.has_duke(2):
            return 1
        else:
            return 0

    def move_piece(self, player):
        if player not in [1,2]:
            raise IndexError("Player must be 1 or 2")
        pieces = self.game.player_pieces[player]
        piece_list = []
        for num, piece in enumerate(pieces):
            print(str(num) + ":", pieces[piece].whoami())
            piece_list.append(piece)
        piece_choice = int(input("Which piece? "))
        piece_id = piece_list[piece_choice]
        piece_obj = pieces[piece_id]
        valid_moves = self.game.filter_moves(piece_id, piece_obj.move())
        if valid_moves:
            for count, move in enumerate(valid_moves):
                print(count, move)
        else:
            print([])
        choice = valid_moves[int(input("Choose an option "))]
        if choice.rule == MoveRule.COMMAND:
            command_choices = piece_obj.moves_with_rule(MoveRule.COMMAND)
            command_choices.remove(choice)
            print("You chose a command move")
            for num, move in enumerate(command_choices):
                print(num, move)

            destination_choice = command_choices[int(input("Choose an option "))]
            self.game.command_movement(piece_obj, choice, destination_choice)
        else:
            self.game.move_piece(piece_obj, choice)
        piece_obj.toggle_side()

    def place_piece_from_bag(self, player):
        piece = self.game.get_piece_from_bag(player)
        self.game.player_pieces[player][id(piece)] = piece

        options_for_placement = self.game.duke_open_sides(player)
        for count, move in enumerate(options_for_placement):
            print(count, move)

        choice = int(input("Choose your position"))
        x, y = options_for_placement[choice]
        
        self.game.place_piece(piece, x, y)



