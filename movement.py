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
    def __init__(self, x, y, rule=MoveRule.NORMAL):
        #TODO: Guarantee types. num, num, MoveType
        self.x = x
        self.y = y
        self.rule = rule 

    def get_x() -> int:
        return self.x

    def get_y():
        return self.y

    def get_rule():
        return self.rule

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+MoveRule.string(self.rule)+")"

