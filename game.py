grid_size = 3
grid0 = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
legal0 = [[i, j] for j in range(grid_size) for i in range(grid_size)]
cells0 = {'w': [], 'b': []}
turn0 = 'b'

grid0[0][0] = 1
grid0[0][1] = 2
legal0.remove([0, 0])
legal0.remove([0, 1])


def next_turn(turn):
    return 'w' if turn == 'b' else 'b'


def get_neighbour(grid, z, connected):
    i, j = z[0], z[1]
    color = grid[i][j]
    neighbour_coord = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0))
    neighbours = []
    for z in neighbour_coord:
        if 0 <= i + z[0] < grid_size and 0 <= j + z[1] < grid_size and \
                grid[i + z[0]][j + z[1]] == color and [i + z[0], j + z[1]] not in connected:
            neighbours.append([i + z[0], j + z[1]])
            connected.append([i + z[0], j + z[1]])
    if not neighbours:
        return []
    return connected + [get_neighbour(grid, neighbours[k], connected) for k in range(len(neighbours))][0]


def update_cells(cells, turn, last_move):
    i, j = last_move[0], last_move[1]
    neighbour_coord = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0))
    new_group = [last_move]
    for z in neighbour_coord:
        for cell in cells[turn]:
            if 0 <= i + z[0] < grid_size and 0 <= j + z[1] < grid_size and [i + z[0], j + z[1]] in cell:
                new_group.extend(cell)
                cells[turn].remove(cell)
    cells[turn].append(new_group)
    return cells


def end_game(cells, turn):
    for cell in cells[turn]:
        if turn == 'w':
            L = [pos[1] for pos in cell]
        else:
            L = [pos[0] for pos in cell]
        if 0 in L and grid_size - 1 in L:
            return True
    return False


def move(grid, legal_moves, cells, turn, pos):
    i, j = pos[0], pos[1]
    grid[i][j] = 1 if turn == 'w' else 2
    legal_moves.remove([i, j])
    return grid, legal_moves, update_cells(cells, turn, pos), next_turn(turn),


def restart_game():
    global grid0, legal0, cells0, turn0
    grid0 = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    legal0 = [[i, j] for j in range(grid_size) for i in range(grid_size)]
    cells0 = {'w': [], 'b': []}
    turn0 = 'b'


def copy(l):
    return [i for i in l]