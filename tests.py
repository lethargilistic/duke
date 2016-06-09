import logging
import sys
import unittest
import inspect
from pieces import *
from duke import Game

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def is_board_valid(self):
        either_player = dict(list(self.game.player_pieces[1].items()) + list(self.game.player_pieces[2].items()))
        for row in self.game.board:
            for cell in row:
                if isinstance(cell, int):
                    if not cell in either_player:
                        return False
                elif not cell == Game.BLANK_TILE:
                    return False
        return True

    def log_movesets(self, result_set, correct_set):
        log = logging.getLogger(inspect.stack()[1].function)
        log.debug("Result set:")
        for move in result_set:
            log.debug(str(move))
        log.debug("Correct set:")
        for move in correct_set:
            log.debug(str(move))

    def test_valid_create_player_1__rightDuke12(self):
        self.game.create_player(1, True, {1,2})
        self.assertTrue(isinstance(self.game.player_pieces[1][self.game.board[0][2]], Duke))
        self.assertTrue(isinstance(self.game.player_pieces[1][self.game.board[0][1]], Footman))
        self.assertTrue(isinstance(self.game.player_pieces[1][self.game.board[1][2]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_valid_create_player_1__leftDuke12(self):
        self.game.create_player(1, False, {1,2})
        self.assertTrue(isinstance(self.game.player_pieces[1][self.game.board[0][3]], Duke))
        self.assertTrue(isinstance(self.game.player_pieces[1][self.game.board[0][2]], Footman))
        self.assertTrue(isinstance(self.game.player_pieces[1][self.game.board[1][3]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_valid_create_player_2__rightDuke12(self):
        self.game.create_player(2, True, {1,2})
        self.assertTrue(isinstance(self.game.player_pieces[2][self.game.board[5][2]], Duke))
        self.assertTrue(isinstance(self.game.player_pieces[2][self.game.board[5][1]], Footman))
        self.assertTrue(isinstance(self.game.player_pieces[2][self.game.board[4][2]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_valid_create_player_2__leftDuke12(self):
        self.game.create_player(2, False, {1,2})
        self.assertTrue(isinstance(self.game.player_pieces[2][self.game.board[5][3]], Duke))
        self.assertTrue(isinstance(self.game.player_pieces[2][self.game.board[5][2]], Footman))
        self.assertTrue(isinstance(self.game.player_pieces[2][self.game.board[4][3]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_invalid_create_player__badPlayer(self):
        with self.assertRaises(ValueError):
            self.game.create_player(3, True, {1,2})

    def test_invalid_create_player_1__badPositions(self):
        with self.assertRaises(ValueError):
            self.game.create_player(1, True, {4,2})

    def test_constructor(self):
        self.assertEqual(1, self.game.current_player)
        self.assertTrue(self.is_board_valid())

    def test_filter_moves_normal__outOfBounds(self):
        footman = Footman(1)
        self.game.place_piece(footman, 1, 0)

        result_moves = set(self.game.filter_moves(id(footman), footman.move2()))
        correct_moves = {Move(1,1), Move(-1,1), Move(0,2)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_normal__friendlyTarget(self):
        footman = Footman(1)
        self.game.place_piece(footman, 1, 0)
        pikeman = Pikeman(1)
        self.game.place_piece(pikeman, 1, 2)

        result_moves = set(self.game.filter_moves(id(footman), footman.move2()))
        correct_moves = {Move(1,1), Move(-1,1)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_normal__friendlyBlocker(self):
        attacker = Pikeman(1)
        self.game.place_piece(attacker, 0, 3)
        blocker = Footman(1)
        self.game.place_piece(blocker, 0, 2)
        target = Footman(2)
        self.game.place_piece(target, 0, 1)

        result_moves = set(self.game.filter_moves(id(attacker), attacker.move2()))
        correct_moves = {Move(0,1)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_normal__enemyTarget(self):
        attacker = Footman(1)
        self.game.place_piece(attacker, 1, 0)
        pikeman = Pikeman(2)
        self.game.place_piece(pikeman, 1, 2)

        result_moves = set(self.game.filter_moves(id(attacker), attacker.move2()))
        correct_moves = {Move(1,1), Move(-1,1), Move(0,2)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_normal__enemyBlocker(self):
        attacker = Pikeman(1)
        self.game.place_piece(attacker, 0, 3)
        blocker = Footman(2)
        self.game.place_piece(blocker, 0, 2)
        target = Footman(2)
        self.game.place_piece(target, 0, 1)

        result_moves = set(self.game.filter_moves(id(attacker), attacker.move2()))
        correct_moves = {Move(0,1), Move(0,-1)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_jumpslide__outOfBounds(self):
        assassin = Assassin(1)
        self.game.place_piece(assassin, 3, 3)
        result_moves = set(self.game.filter_moves(id(assassin), assassin.move1()))

        correct_moves = {Move(0,2,MoveRule.JUMPSLIDE), Move(2,-2,MoveRule.JUMPSLIDE),
                         Move(-2,-2,MoveRule.JUMPSLIDE), Move(-3,-3,MoveRule.JUMPSLIDE)}

        self.log_movesets(result_moves, correct_moves)
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_jumpslide__friendlyTarget(self):
        attacker = Assassin(1)
        self.game.place_piece(attacker, 0, 0)
        footman = Footman(1)
        self.game.place_piece(footman, 0, 2)

        result_moves = set(self.game.filter_moves(id(attacker), attacker.move1()))
        correct_moves = {Move(0,3,MoveRule.JUMPSLIDE), Move(0,4,MoveRule.JUMPSLIDE), 
                         Move(0,5,MoveRule.JUMPSLIDE)}
        self.log_movesets(result_moves, correct_moves)
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_jumpslide__enemyTarget(self):
        attacker = Assassin(1)
        self.game.place_piece(attacker, 0, 0)
        footman = Footman(2)
        self.game.place_piece(footman, 0, 2)

        result_moves = set(self.game.filter_moves(id(attacker), attacker.move1()))
        correct_moves = {Move(0,2,MoveRule.JUMPSLIDE), Move(0,3,MoveRule.JUMPSLIDE), 
                         Move(0,4,MoveRule.JUMPSLIDE), Move(0,5,MoveRule.JUMPSLIDE)}
        self.log_movesets(result_moves, correct_moves)
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_slide__outOfBounds(self):
        duke = Duke(1)
        self.game.place_piece(duke, 0, 0)

        result_moves = set(self.game.filter_moves(id(duke), duke.move1()))
        correct_moves = {Move(1,0,MoveRule.SLIDE), Move(2,0,MoveRule.SLIDE),
                         Move(3,0,MoveRule.SLIDE), Move(4,0,MoveRule.SLIDE),
                         Move(5,0,MoveRule.SLIDE)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_slide__friendlyTarget(self):
        duke = Duke(1)
        self.game.place_piece(duke, 0, 0)
        footman = Footman(1)
        self.game.place_piece(footman, 2, 0)

        result_moves = set(self.game.filter_moves(id(duke), duke.move1()))
        correct_moves = {Move(1,0,MoveRule.SLIDE)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_slide__enemyTarget(self):
        duke = Duke(1)
        self.game.place_piece(duke, 0, 0)
        footman = Footman(2)
        self.game.place_piece(footman, 2, 0)

        result_moves = set(self.game.filter_moves(id(duke), duke.move1()))
        correct_moves = {Move(1,0,MoveRule.SLIDE), Move(2,0,MoveRule.SLIDE)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_strike__outOfBounds(self):
        pikeman = Pikeman(1)
        self.game.place_piece(pikeman, 0, 0)

        result_moves = set(self.game.filter_moves(id(pikeman), pikeman.move2()))
        correct_moves = {Move(0,1)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_strike__friendlyTarget(self):
        pikeman = Pikeman(1)
        self.game.place_piece(pikeman, 0, 0)
        footman = Footman(1)
        self.game.place_piece(footman, 1, 2)

        result_moves = set(self.game.filter_moves(id(pikeman), pikeman.move2()))
        correct_moves = {Move(0,1)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_strike__enemyTarget(self):
        pikeman = Pikeman(1)
        self.game.place_piece(pikeman, 0, 0)
        footman = Footman(2)
        self.game.place_piece(footman, 1, 2)

        result_moves = set(self.game.filter_moves(id(pikeman), pikeman.move2()))
        correct_moves = {Move(0,1), Move(1,2,MoveRule.STRIKE)}
        self.assertEqual(result_moves, correct_moves)

if __name__ == "__main__":
    logging.basicConfig(stream=open("log_test.txt", "w"))
    logging.getLogger("test_filter_moves_jumpslide__outOfBounds").setLevel(logging.DEBUG)
    logging.getLogger("test_filter_moves_jumpslide__friendlyTarget").setLevel(logging.DEBUG)
    logging.getLogger("test_filter_moves_jumpslide__enemyTarget").setLevel(logging.DEBUG)
    unittest.main()
