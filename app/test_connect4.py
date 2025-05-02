import unittest

from board import Board, Player


class Connect4Tests(unittest.TestCase):
    def test_horizontal_win_detection(self):
        board = Board()
        player = Player(0)

        for col in range(4):
            board.place_piece(5, col, player)

        self.assertTrue(board.check_winner(5, 3), "Horizontal win not detected")

    def test_invalid_column_input(self):
        board = Board(rows=6, columns=7)
        player = Player(0)
        self.assertFalse(board.is_column_valid(-1), "Negative column should be invalid")
        self.assertFalse(
            board.is_column_valid(8), "Column beyond board width should be invalid"
        )

        for row in range(6):
            board.place_piece(row, 3, player)

        self.assertFalse(board.is_column_valid(3), "Full column should be invalid")


if __name__ == "__main__":
    unittest.main()
