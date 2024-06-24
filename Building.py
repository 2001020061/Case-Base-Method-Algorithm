import pygame
import sys
import random

# Inisialisasi pygame
pygame.init()

# Ukuran kotak dan jumlah kolom dan baris
cell_size = 20
cols = 30
rows = 30

# Ukuran bangunan
BIG_BUILDING_WIDTH = 10
BIG_BUILDING_HEIGHT = 5
MEDIUM_BUILDING_WIDTH = 5
MEDIUM_BUILDING_HEIGHT = 3
SMALL_BUILDING_WIDTH = 2
SMALL_BUILDING_HEIGHT = 2
HOUSE_WIDTH = 1
HOUSE_HEIGHT = 2

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Ukuran window
width = cell_size * cols
height = cell_size * rows

# Membuat window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sel dengan Angka")

# Fungsi untuk menggambar kotak dan angka di dalamnya
def draw_grid(grid):
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if grid[y][x] == 1:
                pygame.draw.rect(window, RED, rect)
                font = pygame.font.Font(None, 8)
                text = font.render("1", True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)
            elif grid[y][x] == 2:
                pygame.draw.rect(window, GREEN, rect)
                font = pygame.font.Font(None, 8)
                text = font.render("2", True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)
            elif grid[y][x] == 3:
                pygame.draw.rect(window, BLUE, rect)
                font = pygame.font.Font(None, 8)
                text = font.render("3", True, WHITE)
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)
            elif grid[y][x] == 4:
                pygame.draw.rect(window, YELLOW, rect)
                font = pygame.font.Font(None, 8)
                text = font.render("4", True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)
            else:
                pygame.draw.rect(window, GRAY, rect, 1)
                font = pygame.font.Font(None, 8)
                text = font.render("0", True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                window.blit(text, text_rect)

# Fungsi untuk menempatkan bangunan besar secara acak
def place_big_building(grid):
    while True:
        start_x = random.randint(0, cols - BIG_BUILDING_WIDTH)
        start_y = random.randint(0, rows - BIG_BUILDING_HEIGHT)
        if check_valid_position(grid, start_x, start_y, BIG_BUILDING_WIDTH, BIG_BUILDING_HEIGHT):
            for y in range(start_y, start_y + BIG_BUILDING_HEIGHT):
                for x in range(start_x, start_x + BIG_BUILDING_WIDTH):
                    grid[y][x] = 1
            break

# Fungsi untuk menempatkan bangunan medium secara acak
def place_medium_buildings(grid):
    for _ in range(4):
        while True:
            start_x = random.randint(0, cols - MEDIUM_BUILDING_WIDTH)
            start_y = random.randint(0, rows - MEDIUM_BUILDING_HEIGHT)
            if check_valid_position(grid, start_x, start_y, MEDIUM_BUILDING_WIDTH, MEDIUM_BUILDING_HEIGHT):
                for y in range(start_y, start_y + MEDIUM_BUILDING_HEIGHT):
                    for x in range(start_x, start_x + MEDIUM_BUILDING_WIDTH):
                        grid[y][x] = 2
                break

# Fungsi untuk menempatkan bangunan kecil secara acak
def place_small_buildings(grid):
    for _ in range(10):
        while True:
            start_x = random.randint(0, cols - SMALL_BUILDING_WIDTH)
            start_y = random.randint(0, rows - SMALL_BUILDING_HEIGHT)
            if check_valid_position(grid, start_x, start_y, SMALL_BUILDING_WIDTH, SMALL_BUILDING_HEIGHT):
                for y in range(start_y, start_y + SMALL_BUILDING_HEIGHT):
                    for x in range(start_x, start_x + SMALL_BUILDING_WIDTH):
                        grid[y][x] = 3
                break

# Fungsi untuk menempatkan bangunan rumah secara acak
def place_house_buildings(grid):
    for _ in range(10):
        while True:
            start_x = random.randint(0, cols - HOUSE_WIDTH)
            start_y = random.randint(0, rows - HOUSE_HEIGHT)
            if check_valid_position(grid, start_x, start_y, HOUSE_WIDTH, HOUSE_HEIGHT):
                for y in range(start_y, start_y + HOUSE_HEIGHT):
                    for x in range(start_x, start_x + HOUSE_WIDTH):
                        grid[y][x] = 4
                break

# Fungsi untuk memeriksa apakah posisi untuk menempatkan bangunan valid
def check_valid_position(grid, start_x, start_y, width, height):
    for y in range(start_y, start_y + height):
        for x in range(start_x, start_x + width):
            if grid[y][x] != 0:
                return False
    return True

# Membuat grid kosong
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Loop utama
def main():
    place_big_building(grid)
    place_medium_buildings(grid)
    place_small_buildings(grid)
    place_house_buildings(grid)
    running = True
    while running:
        window.fill(WHITE)
        draw_grid(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        pygame.display.flip()

if __name__ == "__main__":
    main()
