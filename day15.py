f = open('input_files/day15.txt')
grid = []
instructions = []
for line in f:
    if "#" in line:
        grid.append(list(line.strip()))
    elif line != "\n":
        instructions.append(line.strip())
f.close()

def start_position(g = grid) -> (int, int):
    r, c = 0, 0 
    for row in range(len(g)):
        for col in range(len(g[0])):
            if g[row][col] == "@":
                g[row][col] = "."
                r, c = row, col
                return r, c

def calc_result(grid):
    result = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "[" or grid[row][col] == "O":
                result += (100 * row) + col
    print(result)

def part1():
    r, c = start_position()
    for line in instructions:
        for i in line:
            if i == "^":
                if grid[r-1][c] == ".": # if empty, move
                    r -= 1
                elif grid[r-1][c] == "O": # if box, determine if it can be pushed
                    for j in range(r-1, 0, -1):
                        if grid[j][c] == "#":
                            break
                        if grid[j][c] == ".":
                            grid[j][c], grid[r-1][c] = "O", "."
                            r -= 1
                            break
            elif i == "v":
                if grid[r+1][c] == ".": # if empty, move
                    r += 1
                elif grid[r+1][c] == "O": # if box, determine if it can be pushed
                    for j in range(r+1, len(grid)):
                        if grid[j][c] == "#":
                            break
                        if grid[j][c] == ".":
                            grid[j][c], grid[r+1][c] = "O", "."
                            r += 1
                            break
            elif i == "<":
                if grid[r][c-1] == ".": # if empty, move
                    c -= 1
                elif grid[r][c-1] == "O": # if box, determine if it can be pushed
                    for j in range(c-1, 0, -1):
                        if grid[r][j] == "#":
                            break
                        if grid[r][j] == ".":
                            grid[r][j], grid[r][c-1] = "O", "."
                            c -= 1
                            break
            elif i == ">":
                if grid[r][c+1] == ".": # if empty, move
                    c += 1
                elif grid[r][c+1] == "O": # if box, determine if it can be pushed
                    for j in range(c+1, len(grid[r])):
                        if grid[r][j] == "#":
                            break
                        if grid[r][j] == ".":
                            grid[r][j], grid[r][c+1] = "O", "."
                            c += 1
                            break
    calc_result(grid)

def expand_grid():
    new_grid = []
    for row in grid:
        new_row = []
        for cell in row:
            if cell == "O":
                new_row.extend(["[", "]"])
            elif cell == "@":
                new_row.extend(["@", "."])
            else:
                new_row.extend([cell, cell])
        new_grid.append(new_row)
    return new_grid

def can_move(g, r, c, delta) -> bool:
    if g[r][c] == "]": c -= 1
    if "#" in g[r+delta][c:c+2]:
        return False
    if g[r+delta][c] == "[":
        return can_move(g, r+delta, c, delta)
    if g[r+delta][c] == "]" and not can_move(g, r+delta, c-1, delta):
        return False
    if g[r+delta][c+1] == "[" and not can_move(g, r+delta, c+1, delta):
        return False
    return True

def move(g, r, c, delta):
    if g[r][c] == "]": c -= 1
    if g[r+delta][c] == "[":
        move(g, r+delta, c, delta)
    if g[r+delta][c] == "]":
        move(g, r+delta, c-1, delta)
    if g[r+delta][c+1] == "[":
        move(g, r+delta, c+1, delta)
    g[r+delta][c], g[r][c] = "[", "."
    g[r+delta][c+1], g[r][c+1] = "]", "."

def part2():
    grid = expand_grid()
    r, c = start_position(grid)
    for line in instructions:
        for i in line:
            if i == "<":
                if grid[r][c-1] == ".": # if empty, move
                    c -= 1
                elif grid[r][c-1] == "]": # if box, determine if it can be pushed
                    for j in range(c-1, 0, -1):
                        if grid[r][j] == "#":
                            break
                        if grid[r][j] == ".":
                            grid[r][j:c-1] = grid[r][j+1:c]
                            grid[r][c-1] = "."
                            c -= 1
                            break
            elif i == ">":
                if grid[r][c+1] == ".": # if empty, move
                    c += 1
                elif grid[r][c+1] == "[": # if box, determine if it can be pushed
                    for j in range(c+1, len(grid[r])):
                        if grid[r][j] == "#":
                            break
                        if grid[r][j] == ".":
                            grid[r][c+2:j+1] = grid[r][c+1:j]
                            grid[r][c+1] = "."
                            c += 1
                            break
            else:
                delta = 1 if i == "v" else -1
                if grid[r+delta][c] == ".": # if empty, move
                    r += delta
                elif grid[r+delta][c] == "[" or grid[r+delta][c] == "]": # if box, determine if it can be pushed
                    if can_move(grid, r+delta, c, delta):
                        move(grid, r+delta, c, delta)
                        r += delta
    calc_result(grid)

part2()