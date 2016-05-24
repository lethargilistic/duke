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

    def in_board_bounds(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def normal_filter(self, move, new_x, new_y):
        '''Returns a list of Move if the Move is valid, or an empty list'''
        #Eliminate based on going off the board
        if not self.in_board_bounds(new_x, new_y):
            return []

        #Eliminate based on landing on friendly unit
        if self.board[new_y][new_x] in self.players[self.current_player]:
            return []
    
        return (move)

    def slide_filter(self, move, new_x, new_y):
        '''Converts a Move with MoveRule.SLIDE to the equivalent valid list of Move with
        MoveRule.NORMAL'''
        slide_moves = []
        while self.in_board_bounds(new_x, new_y):
            if isinstance(self.board[new_y][new_x], int):
                if not self.board[new_y][new_x] in self.players[self.current_player]:
                    slide_moves.append(Move(new_x, new_y))
                break
            else:
                slide_moves.append(Move(new_x, new_y))
            new_x += move.get_x()
            new_y += move.get_y()
        return slide_moves


    def filter_moves(self, piece_id, all_moves):
        #TODO: Return all valid, possible moves by this piece
        valid_moveset = []
        for y, row in enumerate(self.board):
            if piece_id in row:
                x = row.index(piece_id)
                for move in all_moves:
                    new_x = x + move.get_x()
                    new_y = y + move.get_y()
                    if move.get_rule() == MoveRule.NORMAL:
                        valid_moveset += self.normal_filter(move, new_x, new_y)
                    elif move.get_rule() == MoveRule.SLIDE:
                        valid_moveset += self.slide_filter(move, new_x, new_y)
                    else:
                        raise NotImplementedError("Only Normal and slide implemented")

        return valid_moveset

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
