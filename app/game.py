import typer
from rich.console import Console

from connect4 import Connect4
from utils import clear_screen

app = typer.Typer()
console = Console()


@app.command()
def play(
    rows: int = typer.Option(6, "--rows", "-r", help="Number of rows in the board"),
    columns: int = typer.Option(
        7, "--columns", "-c", help="Number of columns in the board"
    ),
    win_count: int = typer.Option(
        4, "--win-count", "-w", help="Number of pieces needed in a row to win"
    ),
    player_count: int = typer.Option(
        2, "--players", "-p", help="Number of players (2-5)"
    ),
    animation: bool = typer.Option(
        False, "--animation", "-a", help="Enable animation for dropping pieces"
    ),
    clean_display: bool = typer.Option(
        False,
        "--clean-display",
        "-d",
        help="Show only the current board state (clears terminal between turns)",
    ),
):
    try:
        game = Connect4(
            rows, columns, win_count, player_count, animation, clean_display, console
        )
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return

    if clean_display:
        clear_screen()

    console.print("[bold]Connect 4[/bold]", justify="center")
    console.print(
        f"Connect {win_count} of your pieces in a row to win!", justify="center"
    )
    console.print(
        f"Choose a column (1-{columns}) to drop your piece.\n", justify="center"
    )

    console.print("Players:", justify="center")
    for player in game.players:
        console.print(f"{player.rich_display_name}", justify="center")
    console.print("")

    if animation:
        console.print(
            "[bold green]Animation mode enabled![/bold green]", justify="center"
        )

    if clean_display:
        console.print(
            "[bold blue]Clean display mode enabled![/bold blue]", justify="center"
        )
        console.print("Press Enter to start the game...", justify="center")
        input()
        clear_screen()

    while True:
        game.display_board()

        console.print(f"\nCurrent player: {game.current_player.rich_display_name}")

        valid_move = False
        while not valid_move:
            try:
                column = typer.prompt(
                    f"Choose a column (1-{game.board.columns})", type=int
                )
                column -= 1
                valid_move = game.make_move(column)
                if not valid_move:
                    console.print("[bold red]Invalid move! Try again.[/bold red]")
            except ValueError:
                console.print(
                    f"[bold red]Please enter a number between 1 and {game.board.columns}.[/bold red]"
                )

        if game.winner:
            game.display_board()
            console.print(
                f"\n{game.winner.rich_display_name} wins! Congratulations!",
                style="bold green",
            )
            break

        if game.board.is_full():
            game.display_board()
            console.print("\nIt's a draw! The board is full.", style="bold blue")
            break


if __name__ == "__main__":
    app()
