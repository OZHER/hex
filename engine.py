import game
from random import choice, shuffle
from copy import copy, deepcopy


def drax_brain(grid, legal_moves, turn):
    for move in legal_moves:
        n_grid, n_legal, _, pursuing = game.move(deepcopy(grid), deepcopy(legal_moves), turn, move)
        if not pursuing:
            return False
        for move2 in n_legal:
            n_grid2, n_legal2, _, pursuing2 = game.move(deepcopy(n_grid), deepcopy(n_legal),
                                                        game.next_turn(turn), move2)
            if not pursuing2 or drax_brain(n_grid2, n_legal2, turn):
                break
        else:
            return False
    return True


def newdrax(grid0, legal0, turn0):
    for move0 in legal0:
        grid1, legal1, turn1, proceed1 = game.move(deepcopy(grid0), deepcopy(legal0), turn0, move0)
        if proceed1:
            return move0
        for move1 in legal1:
            grid2, legal2, turn2, proceed2 = game.move(deepcopy(grid1), deepcopy(legal1), turn1, move1)
            if not proceed2 or not newdrax(grid2, legal2, turn2):
                return False
        else:
            return move0


def drax3(grid0, legal0, turn0):
    for move1 in legal0:
        grid1, legal1, turn1, proceed1 = game.move(deepcopy(grid0), deepcopy(legal0), turn0, move1)
        for move2 in legal1:
            grid2, legal2, turn2, proceed2 = game.move(deepcopy(grid1), deepcopy(legal1), turn1, move2)
            if not proceed2:
                break
            for move3 in legal2:
                grid3, legal3, turn3, proceed3 = game.move(deepcopy(grid2), deepcopy(legal2), turn2, move3)
                for move4 in legal3:
                    grid4, legal4, turn4, proceed4 = game.move(deepcopy(grid3), deepcopy(legal3), turn3, move4)
                    if not proceed4:
                        break
                    for move5 in legal4:
                        grid5, legal5, turn5, proceed5 = game.move(deepcopy(grid4), deepcopy(legal4), turn4, move5)
                        for move6 in legal5:
                            grid6, legal6, turn6, proceed6 = game.move(deepcopy(grid5), deepcopy(legal5), turn5, move6)
                            if not proceed6:
                                break
                            for move7 in legal6:
                                grid7, legal7, turn7, proceed7 = game.move(deepcopy(grid6), deepcopy(legal6), turn6, move7)
                                for move8 in legal7:
                                    grid8, legal8, turn8, proceed8 = game.move(deepcopy(grid7), deepcopy(legal7), turn7, move8)
                                    if not proceed8:
                                        break
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
        else:
            return move1
    print('where is my mind')
    return


def drax(grid, legal_moves, turn):
    for move in game.legal0:
        print('considering', move)
        grid, legal_move, turn, playing2 = game.move(deepcopy(game.grid0), deepcopy(game.legal0), game.turn0, move)
        if not playing2:
            return move
        if drax_brain(grid, legal_move, turn):
            return move
    return kevin()


def computer_series(n):
    black_wins = 0
    log = []
    for i in range(n):
        black_wins += 1 if computer_match() == 'b' else -1
        restart_game()
        log.append(black_wins)
    return log


def computer_match():
    draw_environment()
    while playing:
        if turn == 'b':
            drax()
        kevin()
    return 'w' if turn == 'b' else 'b'


def controlled_hex(x, y, turn, grid, legal_moves, depth):
    if depth == 0:
        return are_connected(x, y)
    return [controlled_hex(x, y, 'w' if turn == 'b' else 'b', move(move, grid),
                           legal_moves.remove(move), depth - 1) for move in legal_moves]


def are_connected(x, y):
    return x in get_neighbour(y, [y])


def kevin():
    return choice(game.legal0)
