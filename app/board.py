from rich.table import Table
from rich import box

from player import Player


class Board:
    def __init__(self, rows: int = 6, columns: int = 7, win_count: int = 4):
        self.rows = rows
        self.columns = columns
        self.win_count = win_count
        self.board = [[None for _ in range(columns)] for _ in range(rows)]
        self.moves_count = 0

    def is_column_valid(self, column: int) -> bool:
        return 0 <= column < self.columns and self.board[0][column] is None

    def get_next_empty_row(self, column: int) -> int | None:
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][column] is None:
                return row
        return None

    def place_piece(self, row: int, column: int, player: Player) -> None:
        self.board[row][column] = player
        self.moves_count += 1

    def check_winner(self, row: int, column: int) -> bool:
        directions = [
            [(0, 1), (0, -1)],  # Horizontal
            [(1, 0), (-1, 0)],  # Vertical
            [(1, 1), (-1, -1)],  # Diagonal /
            [(1, -1), (-1, 1)],  # Diagonal \
        ]

        player = self.board[row][column]

        for dir_pair in directions:
            count = 1

            for dx, dy in dir_pair:
                r, c = row, column

                while True:
                    r += dx
                    c += dy

                    if (
                        0 <= r < self.rows
                        and 0 <= c < self.columns
                        and self.board[r][c] == player
                    ):
                        count += 1
                    else:
                        break

            if count >= self.win_count:
                return True

        return False

    def is_full(self) -> bool:
        return self.moves_count == self.rows * self.columns

    def create_table(self) -> Table:
        table = Table(box=box.SIMPLE)

        for col in range(1, self.columns + 1):
            table.add_column(str(col))

        for row in range(self.rows):
            row_data = []
            for col in range(self.columns):
                cell = self.board[row][col]
                if cell is not None:
                    row_data.append(cell.display_color)
                else:
                    row_data.append(" ")
            table.add_row(*row_data)

        return table

    def get_cell(self, row: int, column: int) -> Player | None:
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.board[row][column]
        return None

    def clone(self) -> "Board":
        new_board = Board(self.rows, self.columns, self.win_count)
        new_board.board = [row[:] for row in self.board]
        new_board.moves_count = self.moves_count
        return new_board
