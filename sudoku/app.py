import pygame
import random
import time
import numpy as np

# Constants
WINDOW_SIZE = (540, 600)
GRID_SIZE = 9
CELL_SIZE = 60
MARGIN = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (230, 240, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)


def is_valid(board, row, col, num):
    """Check if a number can be placed at specific position"""
    # Check row
    for x in range(GRID_SIZE):
        if board[row][x] == num:
            return False

    # Check column
    for y in range(GRID_SIZE):
        if board[y][col] == num:
            return False

    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for y in range(box_row, box_row + 3):
        for x in range(box_col, box_col + 3):
            if board[y][x] == num:
                return False

    return True


def solve(board):
    """Solve the Sudoku puzzle using backtracking"""
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle is solved

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            # If placing num doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False


def find_empty(board):
    """Find an empty cell (with 0)"""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return (i, j)
    return None


def generate_puzzle(difficulty=0.6):
    """Generate a Sudoku puzzle with given difficulty (0.0-1.0)"""
    # Start with a solved board
    board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    solve(board)

    # Create a copy to remove numbers from
    puzzle = board.copy()

    # Calculate how many cells to remove
    cells_to_remove = int(GRID_SIZE * GRID_SIZE * difficulty)

    # Remove random cells
    indices = list(range(GRID_SIZE * GRID_SIZE))
    random.shuffle(indices)

    for idx in indices[:cells_to_remove]:
        row, col = idx // GRID_SIZE, idx % GRID_SIZE
        puzzle[row][col] = 0

    return puzzle, board


def run():
    """Run the Sudoku solver application"""
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Sudoku Solver")

    # Fonts
    digit_font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 32)

    # Game states
    puzzle, solution = generate_puzzle()
    board = puzzle.copy()
    original = puzzle.copy()  # Marks original numbers that can't be modified
    selected = None
    solving = False
    solve_speed = 0.05  # seconds between steps
    last_solve_time = 0
    solve_steps = []
    current_step = 0

    def draw_board():
        """Draw the Sudoku board"""
        screen.fill(WHITE)

        # Draw grid
        for i in range(GRID_SIZE + 1):
            line_width = 3 if i % 3 == 0 else 1

            # Horizontal lines
            pygame.draw.line(
                screen,
                BLACK,
                (MARGIN, MARGIN + i * CELL_SIZE),
                (MARGIN + GRID_SIZE * CELL_SIZE, MARGIN + i * CELL_SIZE),
                line_width,
            )

            # Vertical lines
            pygame.draw.line(
                screen,
                BLACK,
                (MARGIN + i * CELL_SIZE, MARGIN),
                (MARGIN + i * CELL_SIZE, MARGIN + GRID_SIZE * CELL_SIZE),
                line_width,
            )

        # Draw cells
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x, y = MARGIN + col * CELL_SIZE, MARGIN + row * CELL_SIZE

                # Highlight selected cell
                if selected == (row, col):
                    pygame.draw.rect(
                        screen, LIGHT_BLUE, (x + 1, y + 1, CELL_SIZE - 1, CELL_SIZE - 1)
                    )

                # Draw number
                if board[row][col] != 0:
                    color = BLUE if original[row][col] != 0 else BLACK
                    text = digit_font.render(str(board[row][col]), True, color)
                    screen.blit(
                        text,
                        (
                            x + CELL_SIZE // 2 - text.get_width() // 2,
                            y + CELL_SIZE // 2 - text.get_height() // 2,
                        ),
                    )

        # Draw buttons
        solve_button = pygame.Rect(MARGIN, MARGIN + GRID_SIZE * CELL_SIZE + 10, 150, 40)
        pygame.draw.rect(screen, GREEN, solve_button)
        text = button_font.render("Solve", True, WHITE)
        screen.blit(
            text,
            (
                solve_button.centerx - text.get_width() // 2,
                solve_button.centery - text.get_height() // 2,
            ),
        )

        new_button = pygame.Rect(
            MARGIN + 170, MARGIN + GRID_SIZE * CELL_SIZE + 10, 150, 40
        )
        pygame.draw.rect(screen, BLUE, new_button)
        text = button_font.render("New Game", True, WHITE)
        screen.blit(
            text,
            (
                new_button.centerx - text.get_width() // 2,
                new_button.centery - text.get_height() // 2,
            ),
        )

        clear_button = pygame.Rect(
            MARGIN + 340, MARGIN + GRID_SIZE * CELL_SIZE + 10, 150, 40
        )
        pygame.draw.rect(screen, RED, clear_button)
        text = button_font.render("Clear", True, WHITE)
        screen.blit(
            text,
            (
                clear_button.centerx - text.get_width() // 2,
                clear_button.centery - text.get_height() // 2,
            ),
        )

    def visual_solve():
        """Prepare steps for visual solving"""
        nonlocal board, solve_steps, current_step

        # Reset to original puzzle
        board = original.copy()
        solve_steps = []

        # Generate solving steps
        def backtrack_with_steps(row=0, col=0):
            if row == GRID_SIZE:
                return True

            next_row = row + (col + 1) // GRID_SIZE
            next_col = (col + 1) % GRID_SIZE

            if original[row][col] != 0:
                return backtrack_with_steps(next_row, next_col)

            for num in range(1, 10):
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    solve_steps.append((row, col, num))

                    if backtrack_with_steps(next_row, next_col):
                        return True

                    board[row][col] = 0
                    solve_steps.append((row, col, 0))

            return False

        backtrack_with_steps()
        current_step = 0

    # Game loop
    running = True
    while running:
        current_time = time.time()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not solving:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    # Check if click is on the grid
                    if (
                        MARGIN <= pos[0] <= MARGIN + GRID_SIZE * CELL_SIZE
                        and MARGIN <= pos[1] <= MARGIN + GRID_SIZE * CELL_SIZE
                    ):
                        # Convert click position to grid coordinates
                        col = (pos[0] - MARGIN) // CELL_SIZE
                        row = (pos[1] - MARGIN) // CELL_SIZE

                        # Select cell if it's not part of the original puzzle
                        if original[row][col] == 0:
                            selected = (row, col)
                        else:
                            selected = None

                    # Check if solve button is clicked
                    solve_button = pygame.Rect(
                        MARGIN, MARGIN + GRID_SIZE * CELL_SIZE + 10, 150, 40
                    )
                    if solve_button.collidepoint(pos):
                        solving = True
                        visual_solve()

                    # Check if new game button is clicked
                    new_button = pygame.Rect(
                        MARGIN + 170, MARGIN + GRID_SIZE * CELL_SIZE + 10, 150, 40
                    )
                    if new_button.collidepoint(pos):
                        puzzle, solution = generate_puzzle()
                        board = puzzle.copy()
                        original = puzzle.copy()
                        selected = None

                    # Check if clear button is clicked
                    clear_button = pygame.Rect(
                        MARGIN + 340, MARGIN + GRID_SIZE * CELL_SIZE + 10, 150, 40
                    )
                    if clear_button.collidepoint(pos):
                        # Reset to original puzzle
                        board = original.copy()
                        selected = None

                if event.type == pygame.KEYDOWN and selected:
                    row, col = selected

                    # Handle digit keys
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        num = event.key - pygame.K_0  # Convert key to number
                        if is_valid(board, row, col, num):
                            board[row][col] = num

                    # Handle delete and backspace
                    elif event.key in [pygame.K_DELETE, pygame.K_BACKSPACE]:
                        board[row][col] = 0

        # Visual solving animation
        if (
            solving
            and current_step < len(solve_steps)
            and current_time - last_solve_time > solve_speed
        ):
            row, col, num = solve_steps[current_step]
            board[row][col] = num
            current_step += 1
            last_solve_time = current_time

            if current_step >= len(solve_steps):
                solving = False

        # Draw everything
        draw_board()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()


if __name__ == "__main__":
    run()
