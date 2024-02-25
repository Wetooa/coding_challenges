import pygame
import random
import copy
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 5
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEIGHBORS = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))

grid = [[int(random.randint(0, 9) < 7) for _ in range(COLS)] for _ in range(ROWS)]


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
    grid_cpy = copy.deepcopy(grid)

    for row in range(ROWS):
        for col in range(COLS):
            n = neighbor_count(grid_cpy, row, col)

            if grid[row][col]:
                grid[row][col] = int(n in [2, 3])
            else:
                grid[row][col] = n == 3


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME OF LIFE")
running = True


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

    pygame.display.flip()

pygame.quit()
sys.exit()
