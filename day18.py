import copy
from collections import deque
import numpy as np

f = open('input_files/day18.txt')
bytes = []
for line in f:
    x, y = line.split(",")
    bytes.append((int(x), int(y)))
f.close()

map = np.zeros((71, 71), dtype=int)
for i in range(1024):
    x, y = bytes[i]
    map[y][x] = -1

def bfs(map):
    queue = deque()
    queue.append((0, 0))
    steps = 0
    map[0][0] = 1
    while len(queue) > 0:
        r, c = queue.pop()
        if (r, c) == (70, 70):
            # print(map[r][c]-1)
            return True
        if c+1 < len(map) and map[r][c+1] == 0:
            map[r][c+1] = map[r][c] + 1
            queue.appendleft((r, c+1))
        if c-1 >= 0 and map[r][c-1] == 0:
            map[r][c-1] = map[r][c] + 1
            queue.appendleft((r, c-1))
        if r+1 < len(map) and map[r+1][c] == 0:
            map[r+1][c] = map[r][c] + 1
            queue.appendleft((r+1, c))
        if r-1 >= 0 and map[r-1][c] == 0:
            map[r-1][c] = map[r][c] + 1
            queue.appendleft((r-1, c))
    return False

for i in range(1024, len(bytes)):
    x, y = bytes[i]
    map[y][x] = -1
    if not bfs(copy.deepcopy(map)):
        print(f"{x},{y}")
        break