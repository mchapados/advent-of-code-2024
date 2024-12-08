import copy

f = open('input_files/day6.txt')
grid = []
for line in f:
    grid.append(list(line.strip()))
f.close()

row, col = 0, 0  # find the starting position
for i in range(len(grid)):
    if "^" in grid[i]:
        row = i
        col = grid[i].index("^")
        break
        
start = [row, col]  # save starting position (for part 2)

direction = "^"
while True: # mark the path
    if direction == "^":
        while row-1 >= 0 and grid[row-1][col] != "#":
            row -= 1
            grid[row][col] = "X"
        direction = ">"
        if row-1 < 0:
            break
    if direction == ">":
        while col+1 < len(grid[0]) and grid[row][col+1] != "#":
            col += 1
            grid[row][col] = "X"
        direction = "v"
        if col+1 >= len(grid[0]):
            break
    if direction == "v":
        while row+1 < len(grid) and grid[row+1][col] != "#":
            row += 1
            grid[row][col] = "X"
        direction = "<"
        if row+1 >= len(grid):
            break
    if direction == "<":
        while col-1 >= 0 and grid[row][col-1] != "#":
            col -= 1
            grid[row][col] = "X"
        direction = "^"
        if col-1 < 0:
            break

result = 0
for line in grid:
    result += line.count("X")
print(result)

# PART 2
def find_loop(r: int, c: int) -> bool:
    g = copy.deepcopy(grid)
    stack = []
    g[r][c] = "#"
    direction = "^"
    row, col = start
    while True:
        if direction == "^":
            while row-1 >= 0 and g[row-1][col] != "#":
                row -= 1
            direction = ">"
            if row-1 < 0: break
        elif direction == ">":
            while col+1 < len(g[0]) and g[row][col+1] != "#":
                col += 1
            direction = "v"
            if col+1 >= len(g[0]): break
        elif direction == "v":
            while row+1 < len(g) and g[row+1][col] != "#":
                row += 1
            direction = "<"
            if row+1 >= len(g): break
        else:
            while col-1 >= 0 and g[row][col-1] != "#":
                col -= 1
            direction = "^"
            if col-1 < 0: break
        
        if g[row][col] != "+":  # if we get to an unvisited node, clear the stack
            g[row][col] = "+"
            stack.clear()
        elif [row, col] in stack:
            return True
        else:   # keep track of the current path
            stack.append([row, col])
    return False

result = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == "X" and (r != start[0] or c != start[1]):  
            result += 1 if find_loop(r, c) else 0
print(result)