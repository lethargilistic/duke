from pieces import *

class Game():
    def __init__(self):
        self.board_size = 6
        self.board = [["  " for x in range(self.board_size)] for y in range(self.board_size)]
        self.current_player = 1
        
        self.players = [None, None, None] #No Player 0
        self.players_bags = [None, None, None]
        self.create_player(1)
        self.create_player(2)

    def create_player(self, player_number):
        right_or_left_for_duke = input("Place Duke on 1) Right or 2) Left?")
        # Place the duke
        if right_or_left_for_duke == "1":
            x = 2
        elif right_or_left_for_duke == "2":
            x = 3
        else:
            raise IndexError("Choose Right or left")
        if player_number == 1:
            y = 0
        elif player_number == 2:
            y = 5
        else:
            raise IndexError("Player should be 1 or 2")

        #TODO: Custom place the Footmen around the Duke

        duke = Duke(player_number)
        footman1 = Footman(player_number)
        footman2 = Footman(player_number)
        self.board[y][x] = id(duke)
        self.board[y][x+1] = id(footman1)
        self.board[y][x-1] = id(footman2)
        self.players[player_number] = {id(duke):duke,
                                       id(footman1):footman1, 
                                       id(footman2):footman2}
        #TODO
        #self.players_bags[player_number] = [

    def filter_moves(self, piece_id, all_moves):
        #TODO: filters only for normal movement now, and does not tell if other
        #pieces are in the way.
        valid_moveset = []
        for y, row in enumerate(self.board):
            if piece_id in row:
                x = row.index(piece_id)
                for move in all_moves:
                    if 0 <= move.get_x() + x < self.board_size \
                        and 0 <= move.get_y() + y < self.board_size:
                            valid_moveset.append(move)

        return valid_moveset
               #TODO: Return all valid, possible moves by this piece

    def make_move(self) -> bool:
        #Choose piece to move OR place a new piece
        #Highlight possible moves
        #Choose move
        print("CHOOSE MOVE")
        #Execute move
        #Is game over?
        #End of turn housekeeping
        #moved_piece.change_side()
        #self.active_player = self.active_player % 2 + 1
        self.current_player %= 2
        self.current_player += 1
        return True

    def place_piece(self, piece, x, y):
        raise NotImplementedError()

    def remove_piece(self, x, y):
        raise NotImplementedError()

    def get_current_player(self):
        return self.current_player

    def get_board_size(self):
        return self.board_size

    def get_player1_pieces(self):
        return self.players[1]

    def get_player2_pieces(self):
        return self.players[2]

    def get_board(self):
        return self.board
