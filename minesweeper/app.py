import pygame
import random
import sys
from typing import List, Tuple

# Constants
GRID_SIZE = 10
CELL_SIZE = 30
MINES_COUNT = 15
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)

# Colors
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)


def generate_board():
    """Generate the minesweeper board with mines and numbers"""
    # Create empty board
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Place mines randomly
    mines_placed = 0
    while mines_placed < MINES_COUNT:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if board[y][x] != -1:  # -1 represents a mine
            board[y][x] = -1
            mines_placed += 1

            # Update numbers around the mine
            for i in range(max(0, y - 1), min(GRID_SIZE, y + 2)):
                for j in range(max(0, x - 1), min(GRID_SIZE, x + 2)):
                    if board[i][j] != -1:  # Don't update mines
                        board[i][j] += 1

    return board


def run():
    """Run the minesweeper game"""
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Minesweeper")

    # Game states
    board = generate_board()
    revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    flagged = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    game_over = False
    game_won = False
    ai_mode = False
    ai_speed = 500  # ms between AI moves

    # Font setup
    font = pygame.font.Font(None, 24)

    def draw_board():
        screen.fill(WHITE)

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if game_over and board[y][x] == -1:
                    # Show all mines when game is over
                    pygame.draw.rect(screen, RED, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)
                elif revealed[y][x]:
                    # Show revealed cell
                    pygame.draw.rect(screen, WHITE, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)

                    if board[y][x] > 0:
                        # Show number
                        text = font.render(str(board[y][x]), True, BLACK)
                        text_rect = text.get_rect(center=rect.center)
                        screen.blit(text, text_rect)
                else:
                    # Unrevealed cell
                    pygame.draw.rect(screen, GRAY, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)

                    if flagged[y][x]:
                        # Draw flag
                        pygame.draw.polygon(
                            screen,
                            RED,
                            [
                                (x * CELL_SIZE + 10, y * CELL_SIZE + 5),
                                (x * CELL_SIZE + 10, y * CELL_SIZE + 20),
                                (x * CELL_SIZE + 20, y * CELL_SIZE + 12.5),
                            ],
                        )

        # Show AI mode status
        ai_text = font.render(
            f"AI Mode: {'ON' if ai_mode else 'OFF'} (Press A to toggle)", True, BLUE
        )
        screen.blit(ai_text, (10, WINDOW_SIZE[1] - 30))

    def reveal_cell(x, y):
        if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
            return

        if revealed[y][x] or flagged[y][x]:
            return

        revealed[y][x] = True

        if board[y][x] == 0:
            # Reveal surrounding cells if current cell is empty
            for i in range(max(0, y - 1), min(GRID_SIZE, y + 2)):
                for j in range(max(0, x - 1), min(GRID_SIZE, x + 2)):
                    reveal_cell(j, i)

    def check_win():
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if board[y][x] != -1 and not revealed[y][x]:
                    return False
        return True

    def get_adjacent_cells(x, y):
        """Get all valid adjacent cells"""
        adjacent = []
        for i in range(max(0, y - 1), min(GRID_SIZE, y + 2)):
            for j in range(max(0, x - 1), min(GRID_SIZE, x + 2)):
                if i != y or j != x:  # Skip the cell itself
                    adjacent.append((j, i))
        return adjacent

    def ai_solver():
        """AI solver for Minesweeper"""
        # First move: select a random cell in the middle area
        if all(not revealed[y][x] for x in range(GRID_SIZE) for y in range(GRID_SIZE)):
            middle_range = range(GRID_SIZE // 4, 3 * GRID_SIZE // 4)
            x, y = random.choice(list(middle_range)), random.choice(list(middle_range))
            return (x, y, "reveal")

        # Basic strategy: check each revealed cell
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if revealed[y][x] and board[y][x] > 0:
                    # Get adjacent cells
                    adjacent_cells = get_adjacent_cells(x, y)

                    # Count flagged and unrevealed cells
                    flagged_count = sum(1 for j, i in adjacent_cells if flagged[i][j])
                    unrevealed = [
                        (j, i)
                        for j, i in adjacent_cells
                        if not revealed[i][j] and not flagged[i][j]
                    ]

                    # If number of flags equals cell value, all other adjacent cells are safe
                    if flagged_count == board[y][x] and unrevealed:
                        j, i = random.choice(unrevealed)
                        return (j, i, "reveal")

                    # If number of unrevealed cells + flags equals cell value, all unrevealed must be mines
                    if len(unrevealed) + flagged_count == board[y][x] and unrevealed:
                        j, i = random.choice(unrevealed)
                        return (j, i, "flag")

        # If no obvious move, try to find a probabilistic safe move
        # Start with cells adjacent to revealed cells
        edge_cells = set()
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if not revealed[y][x] and not flagged[y][x]:
                    if any(
                        revealed[i][j]
                        for j, i in get_adjacent_cells(x, y)
                        if 0 <= i < GRID_SIZE and 0 <= j < GRID_SIZE
                    ):
                        edge_cells.add((x, y))

        # Make a random guess from the edge cells if available
        if edge_cells:
            x, y = random.choice(list(edge_cells))
            return (x, y, "reveal")

        # Last resort: pick a random unrevealed cell
        unrevealed_cells = [
            (x, y)
            for x in range(GRID_SIZE)
            for y in range(GRID_SIZE)
            if not revealed[y][x] and not flagged[y][x]
        ]
        if unrevealed_cells:
            x, y = random.choice(unrevealed_cells)
            return (x, y, "reveal")

        return None  # No moves available

    # First move should be safe
    first_move = True
    last_ai_move_time = 0

    # Game loop
    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # Toggle AI mode
                    ai_mode = not ai_mode

            if not game_over and not game_won:
                if event.type == pygame.MOUSEBUTTONDOWN and not ai_mode:
                    x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE

                    if event.button == 1:  # Left click
                        if not flagged[y][x]:
                            if first_move and board[y][x] == -1:
                                # First click is always safe
                                # Move the mine elsewhere
                                while True:
                                    new_x, new_y = random.randint(
                                        0, GRID_SIZE - 1
                                    ), random.randint(0, GRID_SIZE - 1)
                                    if (new_x != x or new_y != y) and board[new_y][
                                        new_x
                                    ] != -1:
                                        # Update numbers around the old mine position
                                        for i in range(
                                            max(0, y - 1), min(GRID_SIZE, y + 2)
                                        ):
                                            for j in range(
                                                max(0, x - 1), min(GRID_SIZE, x + 2)
                                            ):
                                                if board[i][j] != -1:
                                                    board[i][j] -= 1

                                        # Place the mine in the new position
                                        board[new_y][new_x] = -1

                                        # Update numbers around the new mine position
                                        for i in range(
                                            max(0, new_y - 1), min(GRID_SIZE, new_y + 2)
                                        ):
                                            for j in range(
                                                max(0, new_x - 1),
                                                min(GRID_SIZE, new_x + 2),
                                            ):
                                                if board[i][j] != -1:
                                                    board[i][j] += 1

                                        # Set the original position to appropriate number
                                        board[y][x] = sum(
                                            1
                                            for i in range(
                                                max(0, y - 1), min(GRID_SIZE, y + 2)
                                            )
                                            for j in range(
                                                max(0, x - 1), min(GRID_SIZE, x + 2)
                                            )
                                            if board[i][j] == -1
                                        )
                                        break
                                first_move = False

                            if board[y][x] == -1:
                                # Game over - clicked on mine
                                game_over = True
                            else:
                                reveal_cell(x, y)
                                if check_win():
                                    game_won = True

                    elif event.button == 3:  # Right click
                        if not revealed[y][x]:
                            flagged[y][x] = not flagged[y][x]

        # AI moves
        if (
            ai_mode
            and not game_over
            and not game_won
            and current_time - last_ai_move_time > ai_speed
        ):
            ai_move = ai_solver()
            if ai_move:
                x, y, action = ai_move

                if action == "reveal":
                    if first_move and board[y][x] == -1:
                        # First click is always safe
                        # Move the mine elsewhere
                        while True:
                            new_x, new_y = random.randint(
                                0, GRID_SIZE - 1
                            ), random.randint(0, GRID_SIZE - 1)
                            if (new_x != x or new_y != y) and board[new_y][new_x] != -1:
                                # Update numbers around the old mine position
                                for i in range(max(0, y - 1), min(GRID_SIZE, y + 2)):
                                    for j in range(
                                        max(0, x - 1), min(GRID_SIZE, x + 2)
                                    ):
                                        if board[i][j] != -1:
                                            board[i][j] -= 1

                                # Place the mine in the new position
                                board[new_y][new_x] = -1

                                # Update numbers around the new mine position
                                for i in range(
                                    max(0, new_y - 1), min(GRID_SIZE, new_y + 2)
                                ):
                                    for j in range(
                                        max(0, new_x - 1), min(GRID_SIZE, new_x + 2)
                                    ):
                                        if board[i][j] != -1:
                                            board[i][j] += 1

                                # Set the original position to appropriate number
                                board[y][x] = sum(
                                    1
                                    for i in range(max(0, y - 1), min(GRID_SIZE, y + 2))
                                    for j in range(max(0, x - 1), min(GRID_SIZE, x + 2))
                                    if board[i][j] == -1
                                )
                                break
                        first_move = False

                    if board[y][x] == -1:
                        game_over = True
                    else:
                        reveal_cell(x, y)
                        if check_win():
                            game_won = True

                elif action == "flag":
                    flagged[y][x] = True

                last_ai_move_time = current_time

        # Draw everything
        draw_board()

        # Game over/win message
        if game_over:
            text = font.render("Game Over! Press R to restart", True, RED)
            screen.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, 10))
        elif game_won:
            text = font.render("You Win! Press R to restart", True, GREEN)
            screen.blit(text, (WINDOW_SIZE[0] // 2 - text.get_width() // 2, 10))

        # Check for restart
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and (game_over or game_won):
            board = generate_board()
            revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
            flagged = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
            game_over = False
            game_won = False
            first_move = True

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()


if __name__ == "__main__":
    run()
