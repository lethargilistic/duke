import unittest
from pieces import *
from duke import Game

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def is_board_valid(self):
        either_player = dict(list(self.game.players[1].items()) + list(self.game.players[2].items()))
        for y, row in enumerate(self.game.board):
            for x, col in enumerate(row):
                space = self.game.board[y][x]
                if isinstance(space, int):
                    if not space in either_player:
                        return False
                elif not space == "  ":
                    return False
        return True

    def test_valid_create_player_1__rightDuke12(self):
        self.game.create_player(1, True, {1,2})
        self.assertTrue(isinstance(self.game.players[1][self.game.board[0][2]], Duke))
        self.assertTrue(isinstance(self.game.players[1][self.game.board[0][1]], Footman))
        self.assertTrue(isinstance(self.game.players[1][self.game.board[1][2]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_valid_create_player_1__leftDuke12(self):
        self.game.create_player(1, False, {1,2})
        self.assertTrue(isinstance(self.game.players[1][self.game.board[0][3]], Duke))
        self.assertTrue(isinstance(self.game.players[1][self.game.board[0][2]], Footman))
        self.assertTrue(isinstance(self.game.players[1][self.game.board[1][3]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_valid_create_player_2__rightDuke12(self):
        self.game.create_player(2, True, {1,2})
        self.assertTrue(isinstance(self.game.players[2][self.game.board[5][2]], Duke))
        self.assertTrue(isinstance(self.game.players[2][self.game.board[5][1]], Footman))
        self.assertTrue(isinstance(self.game.players[2][self.game.board[4][2]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_valid_create_player_2__leftDuke12(self):
        self.game.create_player(2, False, {1,2})
        self.assertTrue(isinstance(self.game.players[2][self.game.board[5][3]], Duke))
        self.assertTrue(isinstance(self.game.players[2][self.game.board[5][2]], Footman))
        self.assertTrue(isinstance(self.game.players[2][self.game.board[4][3]], Footman))
        self.assertTrue(self.is_board_valid())

    def test_invalid_create_player__badPlayer(self):
        with self.assertRaises(ValueError):
            self.game.create_player(3, True, {1,2})

    def test_invalid_create_player_1__badPositions(self):
        with self.assertRaises(ValueError):
            self.game.create_player(1, True, {4,2})

    def test_constructor(self):
        self.assertEqual(1, self.game.current_player)
        self.assertTrue(self.is_board_valid)

