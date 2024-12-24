import numpy as np
from collections import deque

f = open('input_files/day20.txt')
map = []
for line in f:
    map.append(list(line.strip()))
f.close()

S = (0, 0)
E = (0, 0)
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == "S":
            S = (r, c)
        if map[r][c] == "E":
            E = (r, c)
    if S != (0, 0) and E != (0, 0):
        break

# record the distance of each cell to E
dp = np.full((len(map), len(map[0])), -1)
dp[E] = 0
r, c = E
while map[r][c] != "S":
    if map[r+1][c] != "#" and dp[r+1][c] == -1:
        dp[r+1][c] = dp[r][c] + 1
        r += 1
    elif map[r-1][c] != "#" and dp[r-1][c] == -1:
        dp[r-1][c] = dp[r][c] + 1
        r -= 1
    elif map[r][c+1] != "#" and dp[r][c+1] == -1:
        dp[r][c+1] = dp[r][c] + 1
        c += 1
    elif map[r][c-1] != "#" and dp[r][c-1] == -1:
        dp[r][c-1] = dp[r][c] + 1
        c -= 1

def cheat(start, distance, x, steps = 2) -> int:
    # BFS from start, stopping after specified number of steps
    global dp
    global S
    cheats = set()
    r, c = start
    queue = deque()
    visited = np.full((len(dp), len(dp[0])), -1)
    visited[start] = 0
    queue.appendleft((r, c))
    while len(queue) > 0:
        r, c = queue.pop()
        if dp[r][c] != -1 and distance+visited[r][c]+dp[r][c] <= dp[S]-x:
            cheats.add((r, c))
        if visited[r][c] == steps:
            continue
        if c+1 < len(dp[0]) and visited[r][c+1] == -1:
            visited[r][c+1] = visited[r][c] + 1
            queue.appendleft((r, c+1))
        if c-1 >= 0 and visited[r][c-1] == -1:
            visited[r][c-1] = visited[r][c] + 1
            queue.appendleft((r, c-1))
        if r+1 < len(dp) and visited[r+1][c] == -1:
            visited[r+1][c] = visited[r][c] + 1
            queue.appendleft((r+1, c))
        if r-1 >= 0 and visited[r-1][c] == -1:
            visited[r-1][c] = visited[r][c] + 1
            queue.appendleft((r-1, c))
    return len(cheats)

r, c = S
cheats = 0
distance = 0
x = 100
while map[r][c] != "E" and distance <= dp[S]-x:
    cheats += cheat((r, c), distance, x, 20)
    map[r][c] = "x" # record visited cells so we don't backtrack
    if map[r+1][c] != "#" and map[r+1][c] != "x":
        r += 1
    elif map[r-1][c] != "#" and map[r-1][c] != "x":
        r -= 1
    elif map[r][c+1] != "#" and map[r][c+1] != "x":
        c += 1
    elif map[r][c-1] != "#" and map[r][c-1] != "x":
        c -= 1
    distance += 1
print(cheats)