"""
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a
shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left
corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a
block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as
D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in.
The top-left corner is always safe. Output the minimum number of steps to get to the treasure.
"""
from collections import deque

treasure_map = [['O', 'O', 'O', 'O'],
                ['D', 'O', 'D', 'O'],
                ['O', 'O', 'O', 'O'],
                ['X', 'D', 'D', 'O']]

##############
rows = len(treasure_map)
cols = len(treasure_map[0])


def get_treasure_coords():
    for i, row in enumerate(treasure_map):
        for j, ch in enumerate(row):
            if ch == 'X':
                return j, i


def is_position_valid(position):
    x, y = position
    if x < 0 or x >= cols:
        return False
    if y < 0 or y >= rows:
        return False
    if treasure_map[y][x] == 'D':
        return False
    return True


moving_directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
treasure_pos = get_treasure_coords()

visited_positions = set()

queue = deque()
queue.append((0, 0))
parents = {}


def bfs(current_pos):
    print(current_pos)
    visited_positions.add(current_pos)
    for direction in moving_directions:
        move_position = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        if move_position == treasure_pos:
            l = deque([current_pos, move_position])
            while current_pos in parents:
                l.appendleft(parents[current_pos])
                current_pos = parents[current_pos]
            return l
        if move_position not in visited_positions and is_position_valid(move_position):
            parents[move_position] = current_pos
            queue.append(move_position)


while True:
    result = bfs(queue.popleft())
    if result is not None:
        print(result)  # deque([(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 3)])
        break
    if not queue:
        print('Impossible :(')
        break
