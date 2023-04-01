import engine
import ui
import game
import pygame as pg
import gamemode as gmd


show_game = True
grid_size = game.grid_size

running = True

pg.init()
ui.draw_environment()
ui.draw_circles([0, 0], 'w')
ui.draw_circles([3, 3], 'b')
pg.display.update()
while running:
    # gmd.user()
    # gmd.engine(engine.kevin, engine.kevin)
    gmd.userengine(engine.drax)
    game.restart_game()
    ui.draw_environment()
    pg.display.update()
    gmd.playing = True
