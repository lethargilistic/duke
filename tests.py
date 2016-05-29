import unittest
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
                elif not cell == "  ":
                    return False
        return True

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

    def test_filter_moves_slide__emptyBoard(self):
        duke = Duke(1)
        self.game.place_piece(duke, 0, 0)

        result_moves = set(self.game.filter_moves(id(duke), duke.move1()))
        correct_moves = {Move(1,0), Move(2,0), Move(3,0), Move(4,0), Move(5,0)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_slide__friendlyCollision(self):
        duke = Duke(1)
        self.game.place_piece(duke, 0, 0)
        footman = Footman(1)
        self.game.place_piece(footman, 2, 0)

        result_moves = set(self.game.filter_moves(id(duke), duke.move1()))
        correct_moves = {Move(1,0)}
        self.assertEqual(result_moves, correct_moves)

    def test_filter_moves_slide__enemyCollision(self):
        duke = Duke(1)
        self.game.place_piece(duke, 0, 0)
        footman = Footman(2)
        self.game.place_piece(footman, 2, 0)

        result_moves = set(self.game.filter_moves(id(duke), duke.move1()))
        correct_moves = {Move(1,0), Move(2,0)}
        self.assertEqual(result_moves, correct_moves)
