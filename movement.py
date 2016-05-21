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

