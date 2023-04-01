import pstats

import game
from random import choice, shuffle
from copy import deepcopy
import cProfile


def drax_brain(grid, legal_moves, cells, turn):
    for move in legal_moves:
        n_grid, n_legal, n_cells, _ = game.move(copygrid(grid), copylegal(legal_moves), copycells(cells), turn, move)
        if game.end_game(n_cells, turn):
            return False
        for move2 in n_legal:
            n_grid2, n_legal2, n_cells2, _ = game.move(copygrid(n_grid), copylegal(n_legal), copycells(n_cells),
                                                       game.next_turn(turn), move2)
            if game.end_game(n_cells2, game.next_turn(turn)) or drax_brain(n_grid2, n_legal2, n_cells2, turn):
                break
        else:
            return False
    return True


def drax(grid0, legal_moves0, turn0):
    for move in game.legal0:
        print('considering', move)
        grid, legal_move, cells, turn = game.move(copygrid(game.grid0), copylegal(game.legal0), copycells(game.cells0), game.turn0, move)
        if game.end_game(cells, game.next_turn(turn)):
            return move

        with cProfile.Profile() as pr:
            if drax_brain(grid, legal_move, cells, turn):
                stats = pstats.Stats(pr)
                stats.sort_stats(pstats.SortKey.TIME)
                stats.print_stats()
                return move
            else:
                stats = pstats.Stats(pr)
                stats.sort_stats(pstats.SortKey.TIME)
                stats.print_stats()
    return kevin()


def controlled_hex(x, y, turn, grid, legal_moves, depth):
    if depth == 0:
        return are_connected(x, y)
    return [controlled_hex(x, y, 'w' if turn == 'b' else 'b', move(move, grid),
                           legal_moves.remove(move), depth - 1) for move in legal_moves]


def are_connected(x, y):
    return x in get_neighbour(y, [y])


def kevin():
    return choice(game.legal0)


def copylegal(l):
    return [i for i in l]

def copygrid(l):
    return [[j for j in i] for i in l]

def copycells(l):
    return {'w': copygrid(l['w']), 'b': copygrid(l['b'])}
