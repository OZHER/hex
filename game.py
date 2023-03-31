grid_size = 4
grid0 = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
legal0 = [[i, j] for j in range(grid_size) for i in range(grid_size)]
grid0[0][0] = 1
grid0[0][1] = 2
grid0[3][3] = 1
legal0.remove([0, 0])
legal0.remove([0, 1])
legal0.remove([3, 3])
turn0 = 'b'


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


def end_game(grid, l):
    color = 'w' if grid[l[0]][l[1]] == 1 else 'b'
    neigh = get_neighbour(grid, l, [l])
    if color == 'w':
        L = [neigh[i][1] for i in range(len(neigh))]
    else:
        L = [neigh[i][0] for i in range(len(neigh))]
    if 0 in L and grid_size - 1 in L:
        return True
    return False


def move(grid, legal_moves, turn, pos):
    i, j = pos[0], pos[1]
    grid[i][j] = 1 if turn == 'w' else 2
    legal_moves.remove([i, j])
    return grid, legal_moves, next_turn(turn), not end_game(grid, pos)


def restart_game():
    global grid0, legal0, turn0
    grid0 = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    legal0 = [[i, j] for j in range(grid_size) for i in range(grid_size)]
    turn0 = 'b'
