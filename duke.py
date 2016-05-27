from pieces import *

class Game():
    def __init__(self):
        self.board_size = 6
        self.board = [["  " for x in range(self.board_size)] for y in range(self.board_size)]
        self.current_player = 1
        
        self.players = [None, None, None] #No Player 0
        self.players_bags = [None, None, None]

    def create_player(self, player_number, duke_on_right: bool,
                      footman_positions: "set of int"):
        # Place the duke
        if duke_on_right:
            x = 2
        else:
            x = 3
        if player_number == 1:
            y = 0
        elif player_number == 2:
            y = 5
        else:
            raise ValueError("Player should be 1 or 2")

        #TODO: Custom place the Footmen around the Duke
        duke = Duke(player_number)
        self.board[y][x] = id(duke)
        #TODO: Footman_positions ex (1,2); make sure they're different, ints 1 2 or 3
        
        if len(footman_positions) != 2:
            raise ValueError("There must be 2 positions for starting footman positions")
        self.players[player_number] = {id(duke):duke}
        
        for position in footman_positions:
            footman = Footman(player_number)
            footman_x = x
            footman_y = y
            if position == 1:
                footman_x = x - 1
            elif position == 2:
                if player_number == 1:
                    footman_y = y + 1
                else:
                    footman_y = y - 1
            elif position == 3:
                footman_x = x + 1
            self.board[footman_y][footman_x] = id(footman)
            self.players[player_number][id(footman)] = footman

        #TODO: Fill player's bag with the other pieces
        #self.players_bags[player_number] = [

    def in_board_bounds(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def normal_filter(self, move, new_x, new_y):
        '''Returns a list of Move if the Move is valid (does not go off board,
        does not capture friendly Piece), or an empty list'''
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
                    elif move.get_rule() == MoveRule.STRIKE:
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
        '''Put a piece on the board at position (x,y). Will clobber pieces.'''
        self.board[y][x] = piece

    def remove_piece(self, x, y):
        '''Remove a piece on the board at position (x,y).'''
        self.board[y][x] = "  "

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
