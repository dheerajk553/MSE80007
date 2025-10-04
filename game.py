from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player(input("Enter name for Player 1 (X): "), "X"),
            Player(input("Enter name for Player 2 (O): "), "O")
        ]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def get_move(self):
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if row in range(3) and col in range(3):
                    return row, col
                print("❌ Invalid range. Try again.")
            except ValueError:
                print("❌ Invalid input. Enter numbers only.")

    def play(self):
        self.board.reset_all()
        while True:
            self.board.display()
            player = self.players[self.current_player_index]
            print(f"{player.name}'s turn ({player.symbol})")
            row, col = self.get_move()

            if self.board.update_cell(row, col, player.symbol):
                if self.board.check_winner(player.symbol):
                    self.board.display()
                    print(f"🎉 {player.name} wins!")
                    break
                if self.board.is_full():
                    self.board.display()
                    print("🤝 It's a draw!")
                    break
                self.switch_player()
            else:
                print("⚠️ Cell already taken. Try again.")

        # Ask for replay
        replay = input("🔁 Do you want to play again? (y/n): ").lower()
        if replay == "y":
            self.play()
