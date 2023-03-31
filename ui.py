import pygame as pg
from pygame.gfxdraw import aacircle, filled_circle, aapolygon, filled_polygon
import game

show_game = True
grid_size = game.grid_size

if show_game:
    board_y = 800
    size = board_y / game.grid_size / 3 ** 0.5
    outline_size = 1 / 3 * size

    board_x = size * 3 * game.grid_size - size
    borders = size
    screen_x = board_x + 2 * borders
    screen_y = board_y + 2 * borders

    screen = pg.display.set_mode((screen_x, screen_y))

    grid_pos = [[0 for _ in range(grid_size)] for _ in range(game.grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            grid_pos[i][j] = (borders + 3 / 2 * i * size + 3 / 2 * j * size + size,
                              board_y / 2 + borders + 3 ** 0.5 / 2 * i * size - 3 ** 0.5 / 2 * j * size,
                              size)


def draw_environment():
    screen.fill((230, 230, 230))
    draw_grid()
    draw_borders()


def draw_hex(x, y):
    points = [(x, y), (x + size / 2, y + size * 3 ** 0.5 / 2),
              (x + 3 * size / 2, y + size * 3 ** 0.5 / 2),
              (x + 2 * size, y), (x + 3 * size / 2, y - size * 3 ** 0.5 / 2),
              (x + 1 * size / 2, y - size * 3 ** 0.5 / 2)]
    aapolygon(screen, points, (0, 0, 0))


def draw_grid():
    for i in range(grid_size):
        for j in range(grid_size):
            draw_hex(borders + 3 / 2 * i * size + 3 / 2 * j * size,
                     board_y / 2 + borders + 3 ** 0.5 / 2 * i * size - 3 ** 0.5 / 2 * j * size)


def draw_circles(z, turn):
    x, y = z[0], z[1]
    color = (255, 255, 255) if turn == 'w' else (0, 0, 0)
    filled_circle(screen, int(borders + size + 1.5 * x * size + 3 / 2 * y * size),
                  int(borders + board_y / 2 + 3 ** 0.5 / 2 * x * size - 3 ** 0.5 / 2 * y * size),
                  int(size * 0.6),
                  color)
    aacircle(screen, int(borders + size + 1.5 * x * size + 3 / 2 * y * size),
             int(borders + board_y / 2 + 3 ** 0.5 / 2 * x * size - 3 ** 0.5 / 2 * y * size),
             int(size * 0.6),
             (0, 0, 0))
    pg.display.update()


def stairs():
    l, j, q, p = [], [], [], []
    for i in range(grid_size):
        l.append(
            (borders + i * 3 / 2 * size, board_y / 2 + borders + 3 ** 0.5 / 2 * i * size))
        l.append((borders + (i + 1 / 3) * 3 / 2 * size,
                  board_y / 2 + borders + 3 ** 0.5 / 2 * (i + 1) * size))
    l.append(
        (borders + (grid_size - 1 / 3) * 3 / 2 * size,
         board_y / 2 + borders + 3 ** 0.5 / 2 * grid_size * size))
    l.append((borders + (grid_size - 1 / 3) * 3 / 2 * size,
             board_y / 2 + borders + 3 ** 0.5 / 2 * grid_size * size + 3 ** 0.5 / 2 * outline_size))
    l.append((borders + (grid_size - 2 / 3) * 3 / 2 * size + outline_size / 2,
              board_y / 2 + borders + 3 ** 0.5 / 2 * grid_size * size + 3 ** 0.5 / 2 * outline_size))
    for i in range(grid_size - 1, -1, -1):
        l.append((borders + (i + 1 / 3) * 3 / 2 * size - 1 / 2 * outline_size,
                  board_y / 2 + borders + 3 ** 0.5 / 2 * (
                          i + 1) * size + 3 ** 0.5 / 2 * outline_size))
        l.append((borders + i * 3 / 2 * size - 1 / 2 * outline_size,
                  board_y / 2 + borders + 3 ** 0.5 / 2 * i * size + 3 ** 0.5 / 2 * outline_size))
    l.append((borders - outline_size, board_y / 2 + borders))
    for i in range(len(l)):
        j.append((screen_x - l[i][0], l[i][1]))
        q.append((l[i][0], screen_y - l[i][1]))
        p.append((screen_x - l[i][0], screen_y - l[i][1]))
    return (l, (255, 255, 255)), (j, (0, 0, 0)), (q, (0, 0, 0)), (p, (255, 255, 255))


def draw_borders():
    l = stairs()
    for i in range(4):
        filled_polygon(screen, l[i][0], l[i][1])
        aapolygon(screen, l[i][0], (0, 0, 0))


def pos_to_grid(pos):
    for i in range(grid_size):
        for j in range(grid_size):
            if (pos[0] - grid_pos[i][j][0]) ** 2 + (
                    pos[1] - grid_pos[i][j][1]) ** 2 <= 3 / 4 * size ** 2:
                return [i, j]
    return [-1, -1]

