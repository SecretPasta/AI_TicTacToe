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

    def check_grid_full(self) -> bool:
        for row in self.grid:
            for cell in row:
                if not cell.is_safe:
                    return False
        return True

    def is_over(self) -> bool:
        return

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
        return


def play_tic_tac_toe(grid: Grid, player1: Agent, player2: Agent) -> Agent:
    

    while not grid.check_grid_full():

        move = player2.think(grid)


    return




def main():
    cells = [Cell(Coord(0, 2), True, 'X'), Cell(Coord(1, 1), True, 'X'), Cell(Coord(2, 0), True, 'O')]
    grid = Grid(cells)
    grid.print_grid()


if __name__ == '__main__':
    main()
