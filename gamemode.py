import game
import pygame as pg
import ui
import time
import cProfile

playing = True


def user():
    global playing
    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if (z := ui.pos_to_grid(pg.mouse.get_pos())) in game.legal0 and playing:
                    ui.draw_circles(z, game.turn0)
                    game.grid0, game.legal0, game.cells0, game.turn0 = \
                        game.move(game.grid0, game.legal0, game.cells0, game.turn0, z)
                    playing = not game.end_game(game.cells0, game.next_turn(game.turn0))
                    pg.display.update()


def engine(engine1, engine2):
    global playing
    while playing:
        x = pg.event.get()
        ui.draw_circles(z := engine1(game.grid0, game.legal0, game.turn0), game.turn0)
        game.grid0, game.legal0, game.turn0, playing = game.move(game.grid0, game.legal0, game.turn0, z)
        pg.time.delay(2000)
        if playing:
            ui.draw_circles(z := engine2(), game.turn0)
            game.grid0, game.legal0, game.turn0, playing = game.move(game.grid0, game.legal0, game.turn0, z)
            pg.time.delay(2000)
    print('black won' if game.turn0 == 'w' else 'white won')
    return


def userengine(engine):
    global playing
    while playing:
        if game.turn0 == 'b':
            t1 = time.monotonic()
            z = engine(game.grid0, game.legal0, game.turn0)
            print('z', z)
            print(time.monotonic() - t1)
            ui.draw_circles(z, game.turn0)
            game.grid0, game.legal0, game.cells0, game.turn0 = game.move(game.grid0, game.legal0, game.cells0, game.turn0, z)
        if not game.end_game(game.cells0, game.next_turn(game.turn0)):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if (z := ui.pos_to_grid(pg.mouse.get_pos())) in game.legal0 and playing:
                        ui.draw_circles(z, game.turn0)
                        game.grid0, game.legal0, game.cells0, game.turn0 = game.move(game.grid0, game.legal0, game.cells0, game.turn0, z)
                        pg.display.update()
        playing = not game.end_game(game.cells0, game.next_turn(game.turn0))
    print('black won' if game.turn0 == 'w' else 'white won')

    # game.grid, game.legal_moves, game.current_turn, playing = game.move(game.current_grid, game.current_legal_moves,
    #                                                                    game.current_turn, z := engine.kevin())
    # ui.draw_circles(z, game.current_turn)
    # pg.display.update()
