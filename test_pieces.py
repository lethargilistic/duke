import logging
import movement
import unittest
import inspect
from pieces import *
from duke import Game

class PieceTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_moves_with_rule(self):
        log = logging.getLogger(inspect.stack()[0].function)

        marshall = Marshall(1)
        correct_set = {Move(-1,1,MoveRule.COMMAND), Move(0,1,MoveRule.COMMAND),
                       Move(1,1,MoveRule.COMMAND)}

        result_set = set(marshall.moves_with_rule(MoveRule.COMMAND))
        for move in result_set:
            log.debug(str(move))
        self.assertEqual(result_set, correct_set)

if __name__ == "__main__":
    logging.basicConfig(stream=open("log_test_pieces.txt", "w"))
    logging.getLogger("test_moves_with_rule").setLevel(logging.DEBUG)
    unittest.main()
