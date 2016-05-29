from abc import ABCMeta, abstractmethod
from movement import *

class Piece(metaclass=ABCMeta):
    def __eq__(self, other):
        return isinstance(other, self.__class__) \
            and self.name == other.name \
            and self.side == other.side \
            and self.player == other.player

    def __init__(self, name, player):
        self.name = name
        self.side = 1
        self.player = player

    def __ne__(self, other):
        return not __eq__(other)

    def move(self):
        if self.side == 1:
            return self.move1()
        elif self.side == 2:
            return self.move2()
        else:
            raise IndexError("Pieces have 2 sides")

        if self.player == 2:
            for move in moveset:
                move.for_player2()

        return moveset

    @abstractmethod
    def move1(self):
        '''Return a list of Moves'''
        raise NotImplementedError("Move 1 is not written")

    @abstractmethod
    def move2(self):
        '''Return a list of Moves'''
        raise NotImplementedError("Move 2 is not written")

    def toggle_side(self):
        self.side = self.side % 2 + 1

    def whoami(self):
        return type(self).__name__

    def __str__(self):
        return self.name+str(self.player)

class Assassin(Piece):
    def __init__(self, player):
        Piece.__init__(self, "A", player)

    def move1(self):
        return (Move(0,2,MoveRule.JUMPSLIDE),
                Move(2,-2,MoveRule.JUMPSLIDE), 
                Move(-2,-2,MoveRule.JUMPSLIDE)) 

    def move2(self):
        return (Move(0,-2,MoveRule.JUMPSLIDE),
                Move(2,2,MoveRule.JUMPSLIDE), 
                Move(-2,2,MoveRule.JUMPSLIDE)) 

class Bowman(Piece):
    def __init__(self, player):
        Piece.__init__(self, "S", player)

    def move1(self):
        return (Move(0,1), Move(1,0), Move(-1,0),
                Move(2,0,MoveRule.JUMP), Move(0,-2,MoveRule.JUMP),
                Move(-2,0,MoveRule.Jump))

    def move2(self):
        return (Move(0,1), Move(1,-1), Move(-1,-1),
                Move(0,2,MoveRule.JUMP),Move(1,1,MoveRule.JUMP),
                Move(-1,1,MoveRule.JUMP))


class Champion(Piece):
    def __init__(self, player):
        Piece.__init__(self, "C", player)

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
    def __init__(self, player):
        Piece.__init__(self, "Ḑ", player)

    def move1(self):
        return (Move(1,0), Move(-1,0),
                Move(0,2,MoveRule.STRIKE), Move(2,2,MoveRule.STRIKE),
                Move(-2,2,MoveRule.STRIKE))

    def move2(self):
        return (Move(0,1), Move(0,2), 
                Move(1,2,MoveRule.JUMP), Move(-1,2,MoveRule.JUMP),
                Move(1,-1,MoveRule.SLIDE), Move(-1,-1,MoveRule.SLIDE))


class Duke(Piece):
    def __init__(self, player):
        Piece.__init__(self, "D", player)

    def move1(self):
        return (Move(1,0,MoveRule.SLIDE), Move(-1,0,MoveRule.SLIDE))

    def move2(self):
        return (Move(0,1,MoveRule.SLIDE), Move(0,-1,MoveRule.SLIDE))

class Duchess(Piece):
    def __init__(self, player):
        Piece.__init__(self, "U", player)

    def move1(self):
        return (Move(1,0), Move(-1,0), Move(0,-2),
                Move(-2,0,MoveRule.COMMAND), Move(2,0,MoveRule.COMMAND))

    def move2(self):
        return move1()

class Footman(Piece):
    def __init__(self, player):
        Piece.__init__(self, "F", player)

    def move1(self):
        return (Move(0,1), Move(0,-1), 
                Move(1,0), Move(-1,0))

    def move2(self):
        return (Move(1,1), Move(1,-1), 
                Move(-1,1), Move(-1,-1),
                Move(0,2))

class General(Piece):
    def __init__(self, player):
        Piece.__init__(self, "G", player)

    def move1(self):
        return (Move(0,1), Move(2,0), Move(0,-1), Move(-2,0),
                Move(-1,2,MoveRule.JUMP), Move(1,2,MoveRule.JUMP))

    def move2(self):
        return (Move(0,1), Move(1,0), Move(2,0), Move(-1,0), Move(-2,0),
                Move(-1,2,MoveRule.JUMP), Move(1,2,MoveRule.JUMP),
                Move(1,-1,MoveRule.COMMAND), Move(0,-1,MoveRule.COMMAND),
                Move(-1,-1,MoveRule.COMMAND))

class Knight(Piece):
    def __init__(self, player):
        Piece.__init__(self, "K", player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Longbowman(Piece):
    def __init__(self, player):
        Piece.__init__(self, "L", player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Marshall(Piece):
    def __init__(self, player):
        Piece.__init__(self, "M", player)

    def move1(self):
        return (Move(1,0,MoveRule.SLIDE), Move(-1,0,MoveRule.SLIDE),
                Move(2,2,MoveRule.JUMP), Move(-2,2,MoveRule.JUMP),
                Move(0,-2,MoveRule.JUMP))

    def move2(self):
        return (Move(1,0), Move(1,-1), Move(-1,-1), 
                Move(-1,0), Move(-1,1), Move(0,1),
                Move(1,1), Move(2,0), Move(-2,0))

class Oracle(Piece):
    def __init__(self, player):
        Piece.__init__(self, "O", player)

    def move1(self):
        return (Move(1,1), Move(1,-1), Move(-1,-1), Move(-1,1))

    def move2(self):
        raise NotImplementedError()

class Pikeman(Piece):
    def __init__(self, player):
        Piece.__init__(self, "P", player)

    def move1(self):
        return (Move(1,1), Move(2,2), Move(-1,1), Move(-2,2))

    def move2(self):
        return (Move(0,1), Move(0,-1), Move(0,-2),
                Move(1,2,MoveRule.STRIKE), Move(-1,2,MoveRule.STRIKE))

class Priest(Piece):
    def __init__(self, player):
        Piece.__init__(self, "T", player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Ranger(Piece):
    def __init__(self, player):
        Piece.__init__(self, "R", player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()

class Seer(Piece):
    def __init__(self, player):
        Piece.__init__(self, "S", player)

    def move1(self):
        return (Move(1,1), Move(1,-1), Move(-1,-1), Move(-1,1),
                Move(0,2,MoveRule.JUMP), Move(2,0,MoveRule.JUMP),
                Move(0,-2,MoveRule.JUMP), Move(-2,0,MoveRule.JUMP))

    def move2(self):
        return (Move(1,0), Move(0,-1), Move(-1,0), Move(0,1),
                Move(2,2,MoveRule.JUMP), Move(2,-2,MoveRule.JUMP),
                Move(-2,-2,MoveRule.JUMP), Move(-2,2,MoveRule.JUMP))

class Wizard(Piece):
    def __init__(self, player):
        Piece.__init__(self, "W", player)

    def move1(self):
        return (Move(1,0), Move(1,-1), Move(0,-1),
                Move(-1,-1), Move(-1,0), Move(-1,1), 
                Move(0,1), Move(1,1))

    def move2(self):
        return (Move(2,0,MoveRule.JUMP), Move(2,-2,MoveRule.JUMP), Move(0,-2,MoveRule.JUMP),
                Move(-2,-2,MoveRule.JUMP), Move(-2,0,MoveRule.JUMP), Move(-2,2,MoveRule.JUMP),
                Move(0,-2,MoveRule.JUMP), Move(2,2,MoveRule.JUMP))
'''
class Champion(Piece):
    def __init__(self, player):
        Piece.__init__(self, "C", player)

    def move1(self):
        raise NotImplementedError()

    def move2(self):
        raise NotImplementedError()
'''
