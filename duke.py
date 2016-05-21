class MoveRule():
    NORMAL = 0
    STRIKE = 1
    SLIDE = 2
    JUMPSLIDE = 3 

    @staticmethod
    def string(enum):
        return ["NORMAL", "STRIKE", "SLIDE", "JUMPSLIDE"][enum]

class Move():
    def __init__(self, x, y, rule=MoveRule.NORMAL):
        #TODO: Guarantee types. num, num, bool*3
        self.x = x
        self.y = y
        self.rule = rule 

    def get_x():
        return x

    def get_y():
        return y

    def get_rule():
        return rule

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+MoveRule.string(self.rule)+")"

class Piece():
    def __init__(self, name, x, y, player):
        self.name = name
        self.side = 1
        self.x = x
        self.y = y
        self.player = player

    def move1(self):
        '''Return a list of (x,y,bool) tuples representing relative
        movement/strikes. The bool answers "Is this a strike?" If true, an enemy
        piece there is destroyed, but this piece does not actually move.'''
        raise NotImplementedError("Move 1 is not written")

    def move2(self):
        '''Return a list of (x,y,bool) tuples representing relative
        movement/strikes. The bool answers "Is this a strike?" If true, an enemy
        piece there is destroyed, but this piece does not actually move.'''
        raise NotImplementedError("Move 2 is not written")

    def move_piece(rel_x, rel_y):
        '''Perform movement, adding a positive or negative integer to piece's
        x and/or y'''
        self.x += rel_x
        self.y += rel_y

    def get_position(self):
        '''Return dictionary for position, "x" and "y" are keys'''
        return {"x":self.x, "y":self.y}

    def toggle_side(self):
        self.side = self.side % 2 + 1

    def get_name(self):
        return self.name
    
    def get_player(self):
        return self.player

    def __str__(self):
        return self.get_name()+str(self.get_player())

class Footman(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "F", x, y, player)

    def move1(self):
        return (Move(0,1), Move(0,-1), Move(1,0), Move(-1,0))

    def move2(self):
        return (Move(1,1), Move(1,-1), Move(-1,1), Move(-1,-1),
                Move(0,2))

class Duke(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "D", x, y, player)

    def move1(self):
            return (Move(1,0,MoveRule.SLIDE), Move(-1,0,MoveRule.SLIDE))

    def move2(self):
            return (Move(0,1,MoveRule.SLIDE), Move(0,-1,MoveRule.SLIDE))

class Game():
    def __init__(self):
        self.board_size = 6
        self.active_player = 1
        self.player1 = [Duke(3,0,1), Footman(2,0,1), Footman(4,0,1)]
        self.player2 = [Duke(2,5,2), Footman(1,5,2), Footman(2,4,2)]

    def display_board(self):
        #TODO: Couple this loosely
        board = [["  " for x in range(6)] for y in range(6)]
        for piece in self.player1:
            pos = piece.get_position()
            x = pos["x"]
            y = pos["y"]
            board[y][x] = str(piece)
        for piece in self.player2:
            pos = piece.get_position()
            x = pos["x"]
            y = pos["y"]
            board[y][x] = str(piece)
        count = 0
        for row in board:
            print(str(count), end="")
            count+=1
            for slot in row:
                print(slot + "|", end="")
            print()

    def game_loop(self):
        #Each player has a list of pieces. If no Duke in their pieces, they lose
        still_playing = True
        #TODO: remove temporary import below
        import time
        while(still_playing):
            #Display Board
            self.display_board()
            #Choose piece to move
            #Highlight possible moves
            #Choose move
            print("CHOOSE MOVE")
            time.sleep(2)
            #Execute move
            #Is game over?
            #End of turn housekeeping
            #moved_piece.change_side()
            #self.active_player = self.active_player % 2 + 1
        #Game is over. Show results

g = Game()
g.game_loop()
