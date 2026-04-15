from collections import deque
import copy

# GLOBAL COUNTERS (for report)
backtrack_calls = 0
backtrack_failures = 0


# READ SUDOKU FROM FILE
def read_board(filename):
    """
    Reads a Sudoku board from a text file.
    Each line must contain exactly 9 digits (0-9).
    0 represents an empty cell.
    """
    board = []
    with open(filename, 'r') as file:
        for line in file:
            board.append([int(char) for char in line.strip()])
    return board

# PRINT SUDOKU BOARD
def print_board(board):
    """Prints the Sudoku board in readable format."""
    for row in board:
        print(row)


# GET ALL NEIGHBORS OF A CELL
def get_neighbors(row, col):
    """
    Returns all cells that share:
    - Same row
    - Same column
    - Same 3x3 box
    """
    neighbors = set()

    # Row & Column neighbors
    for i in range(9):
        neighbors.add((row, i))
        neighbors.add((i, col))

    # 3x3 Box neighbors
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            neighbors.add((r, c))

    neighbors.remove((row, col))  # remove itself
    return neighbors

# AC-3 ALGORITHM (ARC CONSISTENCY)
def ac3(domains, neighbors):
    """
    Enforces arc consistency across all variables.
    Reduces domain values before search.
    """
    queue = deque()

    # Add all arcs to queue
    for xi in domains:
        for xj in neighbors[xi]:
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            # If domain becomes empty → failure
            if len(domains[xi]) == 0:
                return False

            # Add all related arcs back to queue
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True


def revise(domains, xi, xj):
    """
    Removes inconsistent values from domain[xi].
    """
    revised = False

    # If neighbor has only one value
    if len(domains[xj]) == 1:
        value = next(iter(domains[xj]))

        if value in domains[xi]:
            domains[xi].remove(value)
            revised = True

    return revised


# FORWARD CHECKING

def forward_check(domains, neighbors, variable, value):
    """
    Removes assigned value from neighbors' domains.
    """
    for neighbor in neighbors[variable]:
        if value in domains[neighbor]:
            domains[neighbor].remove(value)

            # If domain becomes empty → failure
            if len(domains[neighbor]) == 0:
                return False

    return True


# SELECT VARIABLE USING MRV HEURISTIC
def select_unassigned_variable(domains):
    """
    Selects variable with Minimum Remaining Values (MRV).
    """
    unassigned = [var for var in domains if len(domains[var]) > 1]

    if not unassigned:
        return None

    return min(unassigned, key=lambda var: len(domains[var]))


# BACKTRACKING SEARCH
def backtrack(domains, neighbors):
    global backtrack_calls, backtrack_failures

    backtrack_calls += 1

    # Check if solution is complete
    if all(len(domains[var]) == 1 for var in domains):
        return domains

    # Select variable
    variable = select_unassigned_variable(domains)

    # Try each value
    for value in list(domains[variable]):
        new_domains = copy.deepcopy(domains)
        new_domains[variable] = {value}

        # Apply forward checking
        if forward_check(new_domains, neighbors, variable, value):

            # Apply AC-3 after assignment
            if ac3(new_domains, neighbors):
                result = backtrack(new_domains, neighbors)

                if result:
                    return result

    # Failure case
    backtrack_failures += 1
    return None


# SOLVE SUDOKU USING CSP
def solve(board):
    """
    Main function to solve Sudoku using CSP.
    """
    domains = {}
    neighbors = {}

    # Initialize domains
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                domains[(row, col)] = set(range(1, 10))
            else:
                domains[(row, col)] = {board[row][col]}

    # Precompute neighbors
    for row in range(9):
        for col in range(9):
            neighbors[(row, col)] = get_neighbors(row, col)

    # Initial AC-3
    if not ac3(domains, neighbors):
        return None

    # Start backtracking
    result = backtrack(domains, neighbors)

    # Convert domains to final board
    if result:
        solved_board = [[0] * 9 for _ in range(9)]
        for (row, col), value in result.items():
            solved_board[row][col] = next(iter(value))
        return solved_board

    return None


def run(filename):
    global backtrack_calls, backtrack_failures

    backtrack_calls = 0
    backtrack_failures = 0

    board = read_board(filename)
    solution = solve(board)

    print("\n----Solution for", filename,"-----\n")

    if solution:
        print_board(solution)
        print("Backtrack Calls:", backtrack_calls)
        print("Backtrack Failures:", backtrack_failures)
    else:
        print("No solution found (invalid board)")


if __name__ == "__main__":
    run("easy.txt")
    run("medium.txt")
    run("hard.txt")
    run("veryhard.txt")