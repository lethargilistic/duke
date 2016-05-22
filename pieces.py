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

    def get_id(self) -> int:
        return self.get_id

    def __str__(self):
        return self.get_name()+str(self.get_player())

class Assassin(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "A", x, y, player)

    def move1(self):
        return (Move(0,2,MoveRule.JUMPSLIDE),
                Move(2,-2,MoveRule.JUMPSLIDE), 
                Move(-2,-2,MoveRule.JUMPSLIDE)) 

    def move2(self):
        return (Move(0,-2,MoveRule.JUMPSLIDE),
                Move(2,2,MoveRule.JUMPSLIDE), 
                Move(-2,2,MoveRule.JUMPSLIDE)) 

class Bowman(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "S", x, y, player)

    def move1(self):
        return (Move(0,1), Move(1,0), Move(-1,0),
                Move(2,0,MoveRule.JUMP), Move(0,-2,MoveRule.JUMP),
                Move(-2,0,MoveRule.Jump))

    def move2(self):
        return (Move(0,1), Move(1,-1), Move(-1,-1),
                Move(0,2,MoveRule.JUMP),Move(1,1,MoveRule.JUMP),
                Move(-1,1,MoveRule.JUMP))


class Champion(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "C", x, y, player)

    def move1(self):
        return (Move(2,0,MoveRule.JUMP), Move(1,0,MoveRule.NORMAL),
                Move(0,2,MoveRule.JUMP), Move(0,1,MoveRule.NORMAL), 
                Move(-2,0,MoveRule.JUMP), Move(-1,0,MoveRule.NORMAL), 
                Move(0,-2,MoveRule.JUMP), Move(0,-1,MoveRule.NORMAL))

    def move2(self):
        return (Move(2,0,MoveRule.JUMP), Move(1,0,MoveRule.STRIKE),
                Move(0,2,MoveRule.JUMP), Move(0,1,MoveRule.STRIKE), 
                Move(-2,0,MoveRule.JUMP), Move(-1,0,MoveRule.STRIKE), 
                Move(0,-2,MoveRule.JUMP), Move(0,-1,MoveRule.STRIKE))

class Dragoon(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "Ḑ", x, y, player)

    def move1(self):
        return (Move(1,0), Move(-1,0),
                Move(0,2,MoveRule.STRIKE), Move(2,2,MoveRule.STRIKE),
                Move(-2,2,MoveRule.STRIKE))

    def move2(self):
        return (Move(0,1), Move(0,2), 
                Move(1,2,MoveRule.JUMP), Move(-1,2,MoveRule.JUMP),
                Move(1,-1,MoveRule.SLIDE), Move(-1,-1,MoveRule.SLIDE))


class Duke(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "D", x, y, player)

    def move1(self):
        return (Move(1,0,MoveRule.SLIDE), Move(-1,0,MoveRule.SLIDE))

    def move2(self):
        return (Move(0,1,MoveRule.SLIDE), Move(0,-1,MoveRule.SLIDE))

class Duchess(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "U", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Footman(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "F", x, y, player)

    def move1(self):
        return (Move(0,1), Move(0,-1), 
                Move(1,0), Move(-1,0))

    def move2(self):
        return (Move(1,1), Move(1,-1), 
                Move(-1,1), Move(-1,-1),
                Move(0,2))

class General(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "G", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Knight(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "K", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Longbowman(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "K", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Marshall(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "M", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Oracle(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "O", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Pikeman(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "P", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Priest(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "T", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Ranger(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "R", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Seer(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "S", x, y, player)

    def move1(self):
        return (Move(1,1), Move(1,-1), Move(-1,-1), Move(-1,1),
                Move(0,2,MoveRule.JUMP), Move(2,0,MoveRule.JUMP),
                Move(0,-2,MoveRule.JUMP), Move(-2,0,MoveRule.JUMP))

    def move2(self):
        return (Move(1,0), Move(0,-1), Move(-1,0), Move(0,1),
                Move(2,2,MoveRule.JUMP), Move(2,-2,MoveRule.JUMP),
                Move(-2,-2,MoveRule.JUMP), Move(-2,2,MoveRule.JUMP))

class Wizard(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "W", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

'''
class Champion(Piece):
    def __init__(self, x, y, player):
        Piece.__init__(self, "C", x, y, player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()
'''
