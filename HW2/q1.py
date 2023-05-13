class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Cell:
    def __init__(self, coord: Coord, is_safe: bool, symbol: str) -> None:
        self.coord = coord
        self.is_safe = is_safe
        self.symbol = symbol


class Grid:
    def __init__(self, inited_cells: list[Cell]) -> None:
        self.grid = [[Cell(Coord(i, j), False, ' ') for j in range(3)] for i in range(3)]
        for cell in inited_cells:
            self.grid[cell.coord.x][cell.coord.y] = cell

    def make_move(self, cell: Cell) -> None:
        self.grid[cell.coord.x][cell.coord.y] = cell

    def game_over(self) -> bool:
        for row in self.grid:
            for cell in row:
                if cell.symbol == ' ':
                    return False
        return True

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

    def print_grid_debug(self) -> None:
        for row in self.grid:
            for cell in row:
                print(f"({cell.coord.x}, {cell.coord.y}): {cell.symbol}", end=" ")
            print()

    def print_grid(self) -> None:
        print(f"-----------------")
        for row in self.grid:
            for cell in row:
                print(f"| {cell.symbol} |", end=' ')
            print(f"\n-----------------")


class Agent:
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

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


def play_tic_tac_toe(grid: Grid, player1: Agent, player2: Agent) -> Agent:
    flag = False
    while not grid.game_over():
        if flag:
            current_player = player1
            flag = not flag
        else:
            current_player = player2
            flag = not flag

        move = current_player.think(grid)
        grid.make_move(move)
        grid.print_grid()

        if grid.is_victory():
            print(f"{current_player.name} is the Winner!")
            break
        elif grid.game_over():
            print("It's a Draw!")

    return current_player


def main():
    # Case B
    cells = [Cell(Coord(0, 2), True, 'X'), Cell(Coord(1, 1), True, 'X'), Cell(Coord(2, 0), True, 'O')]
    grid = Grid(cells)
    grid.print_grid()
    winner = play_tic_tac_toe(grid, Agent("Agent X", "X"), Agent("Agent O", "O"))

    # Case A
    cells2 = [Cell(Coord(0, 0), True, 'X'), Cell(Coord(1, 1), True, 'O'), Cell(Coord(2, 1), True, 'x')]
    grid2 = Grid(cells2)
    grid2.print_grid()
    winner2 = play_tic_tac_toe(grid2, Agent("Agent X", "X"), Agent("Agent O", "O"))


if __name__ == '__main__':
    main()
