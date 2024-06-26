import pygame
import sys
import random
from collections import deque
import os

# Inisialisasi pygame
pygame.init()

# Ukuran kotak dan jumlah kolom dan baris
cell_size = 4
cols = 150
rows = 150

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_GRAY = (220, 220, 220)

# Ukuran bangunan
BIG_BUILDING_WIDTH = 10
BIG_BUILDING_HEIGHT = 5
MEDIUM_BUILDING_WIDTH = 5
MEDIUM_BUILDING_HEIGHT = 3
SMALL_BUILDING_WIDTH = 2
SMALL_BUILDING_HEIGHT = 2
HOUSE_WIDTH = 1
HOUSE_HEIGHT = 2


# Fungsi untuk menempatkan bangunan besar secara acak
def place_big_building(grid, window):
    global placed_big_buildings
    if placed_big_buildings >= 1:
        return  # Jika sudah ada bangunan besar, keluar dari fungsi
    start_x = random.randint(1, cols - BIG_BUILDING_WIDTH - 1)
    start_y = random.randint(1, rows - BIG_BUILDING_HEIGHT - 1)
    if not check_overlap(grid, start_x, start_y, BIG_BUILDING_WIDTH, BIG_BUILDING_HEIGHT):
        for y in range(start_y, start_y + BIG_BUILDING_HEIGHT):
            for x in range(start_x, start_x + BIG_BUILDING_WIDTH):
                grid[y][x] = 1
        placed_big_buildings += 1  # Tingkatkan jumlah bangunan besar yang sudah ditempatkan

        # Path ke gambar big_building.jpg
        big_building_path = "big_building.jpg"
        if os.path.exists(big_building_path):
            big_building_image = pygame.image.load(big_building_path)
            big_building_image = pygame.transform.scale(big_building_image, (
            BIG_BUILDING_WIDTH * cell_size, BIG_BUILDING_HEIGHT * cell_size))
            blit_x = start_x * cell_size
            blit_y = start_y * cell_size
            window.blit(big_building_image, (blit_x, blit_y))
            pygame.display.update()


# Fungsi untuk menempatkan bangunan medium secara acak
def place_medium_buildings(grid, window):
    global placed_medium_buildings
    if placed_medium_buildings >= 4:  # Batasi jumlah bangunan medium menjadi empat
        return
    for _ in range(4 - placed_medium_buildings):  # Tambahkan bangunan medium hingga mencapai batas
        start_x = random.randint(1, cols - MEDIUM_BUILDING_WIDTH - 1)
        start_y = random.randint(1, rows - MEDIUM_BUILDING_HEIGHT - 1)
        if not check_overlap(grid, start_x, start_y, MEDIUM_BUILDING_WIDTH, MEDIUM_BUILDING_HEIGHT):
            for y in range(start_y, start_y + MEDIUM_BUILDING_HEIGHT):
                for x in range(start_x, start_x + MEDIUM_BUILDING_WIDTH):
                    grid[y][x] = 2
            placed_medium_buildings += 1  # Tingkatkan jumlah bangunan medium yang sudah ditempatkan

            # Path ke gambar medium_building.jpg
            medium_building_path = "medium_building.jpg"
            if os.path.exists(medium_building_path):
                medium_building_image = pygame.image.load(medium_building_path)
                medium_building_image = pygame.transform.scale(medium_building_image, (
                MEDIUM_BUILDING_WIDTH * cell_size, MEDIUM_BUILDING_HEIGHT * cell_size))
                blit_x = start_x * cell_size
                blit_y = start_y * cell_size
                window.blit(medium_building_image, (blit_x, blit_y))
                pygame.display.update()


# Fungsi untuk menempatkan bangunan kecil secara acak
def place_small_buildings(grid, window):
    for _ in range(10):
        start_x = random.randint(1, cols - SMALL_BUILDING_WIDTH - 1)
        start_y = random.randint(1, rows - SMALL_BUILDING_HEIGHT - 1)
        if not check_overlap(grid, start_x, start_y, SMALL_BUILDING_WIDTH, SMALL_BUILDING_HEIGHT):
            for y in range(start_y, start_y + SMALL_BUILDING_HEIGHT):
                for x in range(start_x, start_x + SMALL_BUILDING_WIDTH):
                    grid[y][x] = 3

            # Path ke gambar small_building.png
            small_building_path = "small_building.jpg"

            # Periksa apakah file gambar ada
            if os.path.exists(small_building_path):
                small_building_image = pygame.image.load(small_building_path)
                small_building_image = pygame.transform.scale(small_building_image, (
                SMALL_BUILDING_WIDTH * cell_size, SMALL_BUILDING_HEIGHT * cell_size))

                # Calculate the position to blit the image
                blit_x = start_x * cell_size
                blit_y = start_y * cell_size

                # Blit the image onto the window surface
                window.blit(small_building_image, (blit_x, blit_y))
                pygame.display.update()


# Fungsi untuk menempatkan bangunan rumah secara acak
def place_house_buildings(grid, window):
    for _ in range(10):
        start_x = random.randint(1, cols - HOUSE_WIDTH - 1)
        start_y = random.randint(1, rows - HOUSE_HEIGHT - 1)
        if not check_overlap(grid, start_x, start_y, HOUSE_WIDTH, HOUSE_HEIGHT):
            for y in range(start_y, start_y + HOUSE_HEIGHT):
                for x in range(start_x, start_x + HOUSE_WIDTH):
                    grid[y][x] = 4

            # Path ke gambar house.png
            house_path = "house.jpg"

            # Periksa apakah file gambar ada
            if os.path.exists(house_path):
                house_image = pygame.image.load(house_path)
                house_image = pygame.transform.scale(house_image, (HOUSE_WIDTH * cell_size, HOUSE_HEIGHT * cell_size))

                # Calculate the position to blit the image
                blit_x = start_x * cell_size
                blit_y = start_y * cell_size

                # Blit the image onto the window surface
                window.blit(house_image, (blit_x, blit_y))
                pygame.display.update()


# Fungsi untuk menambahkan jalan di sekitar bangunan
def add_road(grid, window):
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            if grid[y][x] == 1 or grid[y][x] == 2 or grid[y][x] == 3 or grid[y][x] == 4:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if grid[y + dy][x + dx] == 0:
                            grid[y + dy][x + dx] = 5

    # Path ke gambar road.png
    road_path = "road.png"

    # Periksa apakah file gambar ada
    if os.path.exists(road_path):
        road_image = pygame.image.load(road_path)
        # Scale gambar jalan sesuai dengan ukuran grid yang ditentukan
        road_image = pygame.transform.scale(road_image, (cell_size, cell_size))

        # Loop melalui setiap sel di grid
        for y in range(rows):
            for x in range(cols):
                # Jika sel adalah jalan (nilai 5), gambar jalan ditambahkan
                if grid[y][x] == 5:
                    # Calculate the position to blit the image
                    blit_x = x * cell_size
                    blit_y = y * cell_size
                    # Blit the image onto the window surface
                    window.blit(road_image, (blit_x, blit_y))

    # Path ke gambar empty.png
    empty_path = "empty.jpg"

    # Periksa apakah file gambar ada
    if os.path.exists(empty_path):
        empty_image = pygame.image.load(empty_path)
        # Scale gambar kosong sesuai dengan ukuran grid yang ditentukan
        empty_image = pygame.transform.scale(empty_image, (cell_size, cell_size))

        # Loop melalui setiap sel di grid
        for y in range(rows):
            for x in range(cols):
                # Jika sel adalah kosong (nilai 0), gambar kosong ditambahkan
                if grid[y][x] == 0:
                    # Calculate the position to blit the image
                    blit_x = x * cell_size
                    blit_y = y * cell_size
                    # Blit the image onto the window surface
                    window.blit(empty_image, (blit_x, blit_y))

    # Update tampilan setelah semua gambar jalan dan kosong ditambahkan
    pygame.display.update()


# Fungsi untuk memeriksa tindihan dengan bangunan lain
def check_overlap(grid, start_x, start_y, width, height):
    for y in range(start_y, start_y + height):
        for x in range(start_x, start_x + width):
            if grid[y][x] != 0:
                return True
    return False


# Fungsi untuk memeriksa apakah semua jalan terhubung
def is_road_connected(grid):
    visited = set()
    queue = deque()
    start_x, start_y = -1, -1
    # Temukan titik awal jalan
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 5:
                start_x, start_y = x, y
                break
        if start_x != -1:
            break
    if start_x == -1:
        return False
    queue.append((start_x, start_y))
    visited.add((start_x, start_y))
    # BFS untuk menemukan semua jalan yang terhubung
    while queue:
        current_x, current_y = queue.popleft()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = current_x + dx, current_y + dy
            if 0 <= new_x < cols and 0 <= new_y < rows and grid[new_y][new_x] == 5 and (new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    # Periksa apakah setiap jalan terhubung
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 5 and (x, y) not in visited:
                return False
    return True


# Fungsi untuk menggambar grid dengan memperhitungkan offset
def draw_grid(grid, offset_x, offset_y, window):
    for y in range(rows):
        for x in range(cols):
            rect = pygame.Rect((x - offset_x) * cell_size, (y - offset_y) * cell_size, cell_size, cell_size)
            if 0 <= (x - offset_x) < cols and 0 <= (y - offset_y) < rows:
                if grid[y][x] == 1:
                    pygame.draw.rect(window, RED, rect)
                elif grid[y][x] == 2:
                    pygame.draw.rect(window, GREEN, rect)
                elif grid[y][x] == 3:
                    pygame.draw.rect(window, BLUE, rect)
                elif grid[y][x] == 4:
                    pygame.draw.rect(window, YELLOW, rect)
                elif grid[y][x] == 5:
                    pygame.draw.rect(window, LIGHT_GRAY, rect)
            else:
                pygame.draw.rect(window, WHITE, rect)


# Membuat grid kosong
grid = [[0 for _ in range(cols)] for _ in range(rows)]

# Variabel untuk melacak posisi awal grid yang akan digambar
offset_x = 0
offset_y = 0

# Variabel global untuk melacak jumlah bangunan yang ditempatkan
placed_big_buildings = 0
placed_medium_buildings = 0


# Loop utama
def main():
    global offset_x, offset_y
    # Ukuran window default
    window_width = 600
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    place_big_building(grid, window)
    place_medium_buildings(grid, window)
    place_small_buildings(grid, window)
    place_house_buildings(grid, window)
    add_road(grid, window)
    while not is_road_connected(grid):
        place_big_building(grid, window)
        place_medium_buildings(grid, window)
        place_small_buildings(grid, window)
        place_house_buildings(grid, window)
        add_road(grid, window)
    running = True
    while running:
        window.fill(WHITE)
        # Menggambar grid dengan memperhitungkan offset
        draw_grid(grid, offset_x, offset_y, window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Menggeser tampilan grid dengan tombol panah
                if event.key == pygame.K_LEFT:
                    offset_x += 1
                elif event.key == pygame.K_RIGHT:
                    offset_x -= 1
                elif event.key == pygame.K_UP:
                    offset_y += 1
                elif event.key == pygame.K_DOWN:
                    offset_y -= 1
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

        #pygame.display.update()


if __name__ == "__main__":
    main()
