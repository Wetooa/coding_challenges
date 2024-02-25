import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 1001, 1000
CELL_SIZE = 5
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEIGHBORS = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))

grid = [[0] * COLS for _ in range(ROWS)]
grid[0][-1] = 1

rule = [0, 1, 1, 1, 0, 1, 1, 0]


def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(
                screen,
                BLACK if grid[row][col] else WHITE,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )


def neighbor_count(grid, row, col):
    count = 0
    for dr, dc in NEIGHBORS:
        r = row + dr
        c = col + dc
        if r < ROWS and c < COLS and r >= 0 and c >= 0 and grid[r][c]:
            count += 1
    return count


def update_grid():
    for col in range(COLS):
        n = (
            grid[current_row - 1][(col - 1) % COLS] * 4
            + grid[current_row - 1][col] * 2
            + grid[current_row - 1][(col + 1) % COLS]
        )
        grid[current_row][col] = rule[n]


running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME OF LIFE")
current_row = 1

while running:
    if any(
        event.type == pygame.QUIT
        or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)
        for event in pygame.event.get()
    ):
        running = False

    screen.fill(WHITE)

    draw_grid()
    update_grid()
    current_row += 1

    pygame.display.flip()

pygame.quit()
sys.exit()
