import pstats

import game
from random import choice, shuffle
import cProfile


def drax_brain(grid, legal_moves, cells, turn):
    for move in legal_moves:
        grid1, legal1, cells1, _ = game.move(copy_grid(grid), copy_legal(legal_moves), copy_cells(cells), turn, move)
        if game.end_game(cells1, turn):
            return False
        for move2 in legal1:
            grid2, legal2, cells2, _ = game.move(copy_grid(grid1), copy_legal(legal1), copy_cells(cells1),
                                                 game.next_turn(turn), move2)
            if game.end_game(cells2, game.next_turn(turn)) or drax_brain(grid2, legal2, cells2, turn):
                break
        else:
            return False
    return True


def drax(grid0, legal_moves0, turn0):
    for move in game.legal0:
        print('considering', move)
        grid, legal_move, cells, turn = game.move(copy_grid(game.grid0), copy_legal(game.legal0), copy_cells(game.cells0), game.turn0, move)
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
    return x in game.get_neighbour(y, [y])


def kevin():
    return choice(game.legal0)


def copy_legal(x):
    return [i for i in x]


def copy_grid(x):
    return [[j for j in i] for i in x]


def copy_cells(x):
    return {'w': copy_grid(x['w']), 'b': copy_grid(x['b'])}
