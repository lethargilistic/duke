class MoveRule():
    NORMAL = 0
    STRIKE = 1
    JUMP = 2
    SLIDE = 3
    JUMPSLIDE = 4 
    COMMAND = 5
    DREAD = 6
    DEFENSE = 7

    @staticmethod
    def string(enum):
        return ["NORMAL", "STRIKE", "JUMP", "SLIDE", "JUMPSLIDE", "COMMAND", "DREAD", "DEFENSE"][enum]

class Move():
    def __eq__(self, other):
        return self.x == other.x \
            and self.y == other.y \
            and self.rule == other.rule

    def __hash__(self):
        return hash((self.x, self.y, self.rule))

    def __init__(self, x:int, y:int, rule=MoveRule.NORMAL):
        self.x = x
        self.y = y
        self.rule = rule 

    def __ne__(self, other):
        return not __eq__(other)
    
    def for_player2(self):
        self.x *= -1
        self.y *= -1

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+MoveRule.string(self.rule)+")"

