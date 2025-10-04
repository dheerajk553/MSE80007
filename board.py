class Board:
    def __init__(self):
        # Initialize a 3x3 grid with empty spaces
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        # Display the board with row and column indices
        print("\n  0   1   2")
        for i, row in enumerate(self.grid):
            print(f"{i} {' | '.join(row)}")
            if i < 2:
                print("  ---------")

    def update_cell(self, row, col, symbol):
        # Update the cell if it's empty
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Check rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True

        # Check diagonals
        if all(self.grid[i][i] == symbol for i in range(3)):
            return True
        if all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def is_full(self):
        # Return True if board is full
        return all(cell != " " for row in self.grid for cell in row)

    def reset_all(self):
        # Reset the board to empty
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
