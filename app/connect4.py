import time

from rich.console import Console
from rich.live import Live

from board import Board, Player
from utils import clear_screen


class Connect4:
    def __init__(
        self,
        rows: int = 6,
        columns: int = 7,
        win_count: int = 4,
        player_count: int = 2,
        animation: bool = False,
        clean_display: bool = False,
        console: Console = Console(),
    ):
        self.board = Board(rows, columns, win_count)
        self.players = Player.create_players(player_count)
        self.current_player_index = 0
        self.winner = None
        self.animation = animation
        self.clean_display = clean_display
        self.console = console

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    def next_player(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def make_move(self, column: int) -> bool:
        if not self.board.is_column_valid(column):
            return False

        row = self.board.get_next_empty_row(column)
        if row is None:
            return False

        if self.animation:
            self.animate_drop(column, row)
        else:
            self.board.place_piece(row, column, self.current_player)

        if self.board.check_winner(row, column):
            self.winner = self.current_player
            return True

        self.next_player()
        return True

    def animate_drop(self, column: int, target_row: int):
        temp_board = self.board.clone()

        with Live(
            self.board.create_table(), refresh_per_second=30, screen=True
        ) as live:
            for anim_row in range(0, target_row):
                temp_board.place_piece(anim_row, column, self.current_player)
                live.update(temp_board.create_table())

                time.sleep(0.05)
                temp_board.board[anim_row][column] = None

            temp_board.place_piece(target_row, column, self.current_player)
            live.update(temp_board.create_table())

            time.sleep(0.1)

        self.board.place_piece(target_row, column, self.current_player)

    def display_board(self):
        if self.clean_display:
            clear_screen()
        self.console.print(self.board.create_table())
