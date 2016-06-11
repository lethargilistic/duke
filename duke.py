from pieces import *
import math
import random

class Game():
    BOARD_SIZE = 6
    BLANK_TILE = "  "
    def __init__(self):
        self.board = [[Game.BLANK_TILE for x in range(Game.BOARD_SIZE)] for y in range(Game.BOARD_SIZE)]
        self.current_player = 1
        
        self.player_pieces = [None, dict(), dict()] #No Player 0
        self.player_bag = [None, dict(), dict()]

    def create_player(self, player_number:int,
                      duke_on_right:bool, footman_positions:"set of Move"):
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

        duke = Duke(player_number)
        self.board[y][x] = id(duke)
        
        if len(footman_positions) != 2 or not footman_positions.issubset({1,2,3}):
            raise ValueError("There must be 2 positions for starting footman positions")

        self.player_pieces[player_number] = {id(duke):duke}
        
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
            self.player_pieces[player_number][id(footman)] = footman

        # Fill player's bag with the other pieces
        self.player_bag[player_number] = [General(player_number)]
        '''
        self.player_bag[player_number] = [Footman(player_number),
                            Pikeman(player_number), Pikeman(player_number),
                            Pikeman(player_number), Knight(player_number), 
                            Wizard(player_number), Ranger(player_number),
                            Seer(player_number), General(player_number), 
                            Priest(player_number), Champion(player_number),
                            Marshall(player_number), Bowman(player_number),
                            Dragoon(player_number), Assassin(player_number),
                            Longbowman(player_number)]
        '''

    def __in_board_bounds(self, x, y):
        return 0 <= x < Game.BOARD_SIZE and 0 <= y < Game.BOARD_SIZE

    def __jump_filter(self, move, new_x, new_y) -> "list of Move":
        '''Returns a list of Move if the Move is valid (does not go off board,
        does not capture friendly Piece), or an empty list.'''
        #Eliminate based on going off the board
        if not self.__in_board_bounds(new_x, new_y):
            return []

        #Eliminate based on landing on friendly unit
        if self.board[new_y][new_x] in self.player_pieces[self.current_player]:
            return []
    
        return [move]

    def __normal_filter(self, move, new_x, new_y) -> "list of Move":
        if not self.__in_board_bounds(new_x, new_y):
            return []

        if self.board[new_y][new_x] in self.player_pieces[self.current_player]:
            return []

        #Start at the target cell
        displacement_x = move.x
        displacement_y = move.y

        #Determine direction of move
        sign_of_x = 0
        sign_of_y = 0
        if move.x != 0:
            sign_of_x = int(math.copysign(1, move.x))
        if move.y != 0:
            sign_of_y = int(math.copysign(1, move.y))

        #Move back from target cell toward start cell, checking validity
        displacement_x -= sign_of_x
        displacement_y -= sign_of_y
        #Normal movement will always be on the x, y, or xy axes
        while displacement_x != 0 or displacement_y != 0:
            if isinstance(self.board[new_y-displacement_y][new_x-displacement_x], int):
                return []
            displacement_x -= sign_of_x
            displacement_y -= sign_of_y

        return [move]

    def __slide_filter(self, move, new_x, new_y) -> "list of Move":
        '''Converts a Move with MoveRule.SLIDE to the equivalent valid list of
        Moves for the individual board squares'''
        slide_moves = []
        displacement_x = move.x
        displacement_y = move.y
        while self.__in_board_bounds(new_x, new_y):
            if isinstance(self.board[new_y][new_x], int):
                if self.board[new_y][new_x] not in self.player_pieces[self.current_player]:
                    slide_moves.append(Move(displacement_x, displacement_y, MoveRule.SLIDE))
                break
            else:
                slide_moves.append(Move(displacement_x, displacement_y, MoveRule.SLIDE))
            new_x += move.x
            new_y += move.y
            displacement_x += move.x
            displacement_y += move.y

        return slide_moves
 
    def __jumpslide_filter(self, move, new_x, new_y) -> "list of Move":
        '''Converts a Move with MoveRule.SLIDE to the equivalent valid list of
        Moves for the individual board squares'''
        slide_moves = []
        displacement_x = move.x
        displacement_y = move.y
        sign_of_x = 0
        sign_of_y = 0
        if move.x != 0:
            sign_of_x = int(math.copysign(1, move.x))
        if move.y != 0:
            sign_of_y = int(math.copysign(1, move.y))

        while self.__in_board_bounds(new_x, new_y):
            if not isinstance(self.board[new_y][new_x], int) or self.board[new_y][new_x] not in self.player_pieces[self.current_player]:
                    slide_moves.append(Move(displacement_x, displacement_y, MoveRule.JUMPSLIDE))
            new_x += sign_of_x
            new_y +=  sign_of_y
            displacement_x += sign_of_x
            displacement_y += sign_of_y

        return slide_moves

    def __strike_filter(self, move, new_x, new_y) -> "list of Move":
        '''Returns a list of Move if the move is valid'''
        #Eliminate based on going off the board
        if not self.__in_board_bounds(new_x, new_y):
            return []

        #Eliminate based on landing on friendly unit
        if self.board[new_y][new_x] not in self.player_pieces[self.current_player%2+1]:
            return []
    
        return [move]

    def __command_filter(self, move, new_x, new_y) -> "list of Move":
        if self.__in_board_bounds(new_x, new_y) and self.board[new_y][new_x] in self.player_pieces[self.current_player]:
            return [move]
        else:
            return []

    def filter_moves(self, piece_id, all_moves) -> "list of Move":
        #TODO: Return all valid, possible moves by this piece
        valid_moveset = []
        for y, row in enumerate(self.board):
            if piece_id in row:
                x = row.index(piece_id)
                for move in all_moves:
                    new_x = x + move.x
                    new_y = y + move.y
                    if move.rule == MoveRule.NORMAL:
                        valid_moveset += self.__normal_filter(move, new_x, new_y)
                    elif move.rule == MoveRule.STRIKE:
                        valid_moveset += self.__strike_filter(move, new_x, new_y)
                    elif move.rule == MoveRule.JUMP:
                        valid_moveset += self.__jump_filter(move, new_x, new_y)
                    elif move.rule == MoveRule.SLIDE:
                        valid_moveset += self.__slide_filter(move, new_x, new_y)
                    elif move.rule == MoveRule.JUMPSLIDE:
                        valid_moveset += self.__jumpslide_filter(move, new_x, new_y)
                    elif move.rule == MoveRule.COMMAND:
                        valid_moveset += self.__command_filter(move, new_x, new_y)
                    elif move.rule == MoveRule.DREAD:
                        raise NotImplementedError("Not all move filtering is implemented")
                    elif move.rule == MoveRule.DEFENSE:
                        raise NotImplementedError("Not all move filtering is implemented")
                    else:
                        raise NotImplementedError("Not all move filtering is implemented")

        return valid_moveset

    def command_movement(self, piece_with_command, source_command, destination_command):
        '''Move the piece at source_command.(x,y) to destination_command.(x,y)'''
        x, y = self.find_piece(piece_with_command)
        player = piece_with_command.player
        piece_moved = self.player_pieces[player][self.board[y+source_command.y][x+source_command.x]]
        self.board[y+source_command.y][x+source_command.x] = Game.BLANK_TILE
        

        self.place_piece(piece_moved,
                         x+destination_command.x, y+destination_command.y)

    def place_piece(self, piece, x, y):
        '''Put a piece on the board at position (x,y). Will clobber pieces.'''
        self.board[y][x] = id(piece)
        self.player_pieces[piece.player][id(piece)] = piece

    def find_piece(self, piece):
        for y, row in enumerate(self.board):
            if id(piece) in row:
                return row.index(id(piece)), y
        return None

    def has_duke(self, player:int):
        for piece_id in self.player_pieces[player]:
            if isinstance(self.player_pieces[player][piece_id], Duke):
                return True
        return False

    def get_piece_from_bag(self, player):
        bag_len = len(self.player_bag[player])
        return self.player_bag[player].pop(random.randrange(0, bag_len))

    def duke_open_sides(self, player):
        open_cells = []

        duke = None
        for ids in self.player_pieces[player]:
            if isinstance(self.player_pieces[player][ids], Duke):
               duke = self.player_pieces[player][ids]
               break
        if duke:
            x, y = self.find_piece(duke)
            for i in [(0,1), (1,0), (0, -1), (-1, 0)]:
                if self.__in_board_bounds(x+i[0], y+i[1]) and not isinstance(self.board[y+i[1]][x+i[0]], int):
                    open_cells.append((x+i[0], y+i[1]))
        
        return open_cells

    def move_piece(self, piece, move):
        x, y = self.find_piece(piece)
        self.board[y][x] = Game.BLANK_TILE
        new_x = x + move.x
        new_y = y + move.y
        if isinstance(self.board[new_y][new_x], int):
            other_piece_id = self.board[new_y][new_x]
            #TODO: raise exeption if in this player's pieces list, not enemy's
            del self.player_pieces[piece.player%2+1][other_piece_id]
        self.board[new_y][new_x] = id(piece)
        
    def destroy_piece(self, x, y):
        '''Remove a piece on the board at position (x,y).'''
        if isinstance(self.board[y][x], int): #int is piece id
            piece_id = self.board[y][x]
            if piece_id in self.player_pieces[1]:
                del self.player_pieces[1][piece_id]
            elif piece_id in self.player_pieces[2]:
                del self.player_pieces[2][piece_id]
            else:
                raise KeyError("Unexpected piece id found in board")
        self.board[y][x] = Game.BLANK_TILE

    def toggle_player(self):
        self.current_player = self.current_player % 2 + 1

    def __str__(self):
        output = ""
        for count, row in enumerate(self.board[::-1]):
            output += str(Game.BOARD_SIZE-count-1)+"|"
            for cell in row:
                if isinstance(cell, int):
                    if cell in self.player_pieces[1]:
                        output += str(self.player_pieces[1][cell]) + "|"
                    elif cell in self.player_pieces[2]:
                        output += str(self.player_pieces[2][cell]) + "|"
                    else:
                        raise ValueError("An id was on the board but not belonging to a player")
                elif cell == Game.BLANK_TILE:
                    output += cell + "|"
                else:
                    raise ValueError("An unexpected element on the board encountered")
            output += "\n"
        return output
