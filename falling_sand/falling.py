import pygame
import copy
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 75, 0)


grid = [[0] * COLS for _ in range(ROWS)]


def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(
                screen,
                BROWN if grid[row][col] == 1 else WHITE,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )


def update():
    global grid
    grid_cpy = copy.deepcopy(grid)

    for i in range(ROWS - 1):
        for j in range(COLS):
            if grid_cpy[i][j]:
                grid[i][j] = 0
                if not grid_cpy[i + 1][j]:
                    grid[i + 1][j] = 1
                elif j > 0 and not grid_cpy[i + 1][j - 1]:
                    grid[i + 1][j - 1] = 1
                elif j < COLS - 1 and not grid_cpy[i + 1][j + 1]:
                    grid[i + 1][j + 1] = 1
                else:
                    grid[i][j] = 1


def toggle_cell(mouse_pos):
    col = mouse_pos[0] // CELL_SIZE
    row = mouse_pos[1] // CELL_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        grid[row][col] = 1


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Falling Sand")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False
        if pygame.mouse.get_pressed()[0]:
            toggle_cell(pygame.mouse.get_pos())

    screen.fill(WHITE)

    draw_grid()
    update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
