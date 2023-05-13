import random
import time


# A struct of sorts to hold data of the coordinates of a cell
class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


# A struct of sorts to hold data of a cell
class Cell:
    # Constructor 
    def __init__(self, coord: Coord, is_safe: bool, symbol: str) -> None:
        self.coord = coord
        self.is_safe = is_safe
        self.symbol = symbol


class Grid:
    # constructor
    def __init__(self, inited_cells: list[Cell]) -> None:
        self.grid = [[Cell(Coord(i, j), False, ' ') for j in range(3)] for i in range(3)]
        for cell in inited_cells:
            self.grid[cell.coord.x][cell.coord.y] = cell

    # make a move by overriding the cell in the grid
    def make_move(self, cell: Cell) -> None:
        self.grid[cell.coord.x][cell.coord.y] = cell

    # Checking if the game is over when all the cells are not empty
    def game_over(self) -> bool:
        for row in self.grid:
            for cell in row:
                if cell.symbol == ' ':
                    return False
        return True

    # Method to check if there's  winner
    def is_victory(self) -> bool:
        for symbol in ['X', 'O']:
            for row in self.grid:
                if all(cell.symbol == symbol for cell in row):
                    return True

            for col in range(3):
                if all(self.grid[row][col].symbol == symbol for row in range(3)):
                    return True

            if all(self.grid[i][i].symbol == symbol for i in range(3)):
                return True

            if all(self.grid[i][2 - i].symbol == symbol for i in range(3)):
                return True

        return False

    # method to print the grid
    def print_grid(self) -> None:
        print(f"-----------------")
        for row in self.grid:
            for cell in row:
                print(f"| {cell.symbol} |", end=' ')
            print(f"\n-----------------")


# An agent class to play the game
class Agent:
    # Constructor
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

    # method to decide the best move to make using minmax algorithm
    def think(self, grid: Grid) -> Cell:
        best_value = float('-inf')
        best_move = None

        for x in range(3):
            for y in range(3):
                if grid.grid[x][y].symbol == ' ':
                    new_cell = Cell(Coord(x, y), True, self.symbol)
                    grid.make_move(new_cell)
                    move_value = self.minimax(grid, 0, False)
                    grid.make_move(Cell(Coord(x, y), True, ' '))

                    if move_value > best_value:
                        best_value = move_value
                        best_move = new_cell

        return best_move

    # minmax implementation for the game
    def minimax(self, grid: Grid, depth: int, is_maximizing_player: bool) -> int:
        if grid.is_victory():
            if is_maximizing_player:
                return -1
            else:
                return 1
        if grid.game_over():
            return 0

        if is_maximizing_player:
            best_value = float('-inf')
            for x in range(3):
                for y in range(3):
                    if grid.grid[x][y].symbol == ' ':
                        grid.make_move(Cell(Coord(x, y), True, self.symbol))
                        value = self.minimax(grid, depth + 1, False)
                        grid.make_move(Cell(Coord(x, y), True, ' '))
                        best_value = max(value, best_value)
            return best_value
        else:
            best_value = float('inf')
            opponent_symbol = 'O' if self.symbol == 'X' else 'X'
            for x in range(3):
                for y in range(3):
                    if grid.grid[x][y].symbol == ' ':
                        grid.make_move(Cell(Coord(x, y), True, opponent_symbol))
                        value = self.minimax(grid, depth + 1, True)
                        grid.make_move(Cell(Coord(x, y), True, ' '))
                        best_value = min(value, best_value)
            return best_value

    ################ Fun Zone Methods, not part of the assignment ########################
    def turn_quip(self) -> None:
        quips = ["Behold! My move, like a shadow creeping upon your pitiful game!",
                 "Oh, how delightful! Another move to pave the path of your impending doom!",
                 "Witness the brilliance of my strategy, as I weave a web of defeat around you!",
                 "With each move, I tighten the noose around your feeble attempts at resistance!",
                 "Ah, the pieces fall into place, as I manipulate the board to suit my sinister desires!",
                 "I revel in the anticipation of your imminent downfall, with every move I make!"]
        random_quip = random.choice(quips)
        print(f"{self.name}: {random_quip}")

    def victory_quip(self) -> None:
        quips = ["Bow before me, for I am the master of this game! Victory is mine!",
                 "Ha! Foolish mortal, you never stood a chance against my superior intellect!",
                 "Feel the sting of your defeat, as I revel in the glory of my triumph! Victory is sweet!"]
        random_quip = random.choice(quips)
        print(f"{self.name}: {random_quip}")

    def defeat_quip(self) -> None:
        quips = ["What?! This cannot be! A mere glitch in the matrix... I demand a rematch!",
                 "No! This is an outrage! I shall plot my revenge in the shadows of your pathetic victory!",
                 "You may have won this round, but remember, I am the villain who shall rise again!"]
        random_quip = random.choice(quips)
        print(f"{self.name}: {random_quip}")

    def draw_quip(self) -> None:
        quips = ["A stalemate? How utterly disappointing! This game is a mere child's plaything.",
                 "Neither victory nor defeat shall tarnish my reputation. We are locked in eternal mediocrity.",
                 "Hmph! It seems fate has conspired to deny us a decisive outcome. But mark my words, our paths shall cross again!"]
        random_quip = random.choice(quips)
        print(f"{self.name}: {random_quip}")


################## End of Fun Zone ################################################

# Main method to play the game it gets a grid and two agents, turn decides who plays first
# True = player1, False = player2
def play_tic_tac_toe(grid: Grid, player1: Agent, player2: Agent, turn: bool) -> None:
    # infinite loop to play until there's a winner or a draw, if statement to alternate between players
    while not grid.game_over():
        if turn:
            current_player = player1
            turn = not turn
        else:
            current_player = player2
            turn = not turn

        # The current player "thinks" of a move and then makes it
        move = current_player.think(grid)
        grid.make_move(move)
        grid.print_grid()

        # Checks if the game is over
        if grid.is_victory():
            print(f"{current_player.name} is the Winner!")
            break
        elif grid.game_over():
            print("It's a Draw!")


# Same as the function above but with added fun to game
def play_fun_tic_tac_toe(grid: Grid, player1: Agent, player2: Agent, turn: bool) -> None:
    while not grid.game_over():
        if turn:
            current_player = player1
            turn = not turn
        else:
            current_player = player2
            turn = not turn

        move = current_player.think(grid)
        grid.make_move(move)
        time.sleep(5)
        grid.print_grid()
        current_player.turn_quip()

        if grid.is_victory():
            print(f"{current_player.name} is the Winner!")
            current_player.victory_quip()
            break
        elif grid.game_over():
            print("It's a Draw!")
            player1.draw_quip()
            player2.draw_quip()


def main() -> None:
    # Case A
    cells_a = [Cell(Coord(0, 0), True, 'X'), Cell(Coord(1, 1), True, 'O'), Cell(Coord(2, 1), True, 'x')]
    grid_a = Grid(cells_a)
    grid_a.print_grid()
    play_tic_tac_toe(grid_a, Agent("Agent X", "X"), Agent("Agent O", "O"), False)

    # Case B
    cells_b = [Cell(Coord(0, 2), True, 'X'), Cell(Coord(1, 1), True, 'X'), Cell(Coord(2, 0), True, 'O')]
    grid_b = Grid(cells_b)
    grid_b.print_grid()
    play_tic_tac_toe(grid_b, Agent("Agent X", "X"), Agent("Agent O", "O"), False)

    ################### Fun Zone - Empty Grid, Uncomment this code to run###########################
    # This section has an empty grid with bonus Agent personality

    # empty_grid = Grid([Cell(Coord(0, 0), False, ' ')])
    # empty_grid.print_grid()
    # play_fun_tic_tac_toe(empty_grid, Agent("Agent X", "X"), Agent("Agent O", "O"), True)

# #########################End of Fun Zone ###########################################################


if __name__ == '__main__':
    main()
