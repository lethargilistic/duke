import movement

class Piece():
    def __init__(self, name, x, y, player):
        self.name = name
        self.side = 1
        self.x = x
        self.y = y
        self.player = player

    def move1(self):
        '''Return a list of Moves'''
        raise NotImplementedError("Move 1 is not written")

    def move2(self):
        '''Return a list of Moves'''
        raise NotImplementedError("Move 2 is not written")

    def move_piece(rel_x, rel_y):
        '''Perform movement, adding a positive or negative integer to piece's
        x and/or y'''
        self.x += rel_x
        self.y += rel_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def toggle_side(self):
        self.side = self.side % 2 + 1

    def get_name(self):
        return self.name
    
    def get_player(self):
        return self.player

    def get_id(self):
        return self.get_id

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


