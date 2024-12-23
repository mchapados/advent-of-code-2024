f = open('input_files/test.txt')
maze = []
for line in f:
    maze.append(list(line.strip()))
f.close()

BEST_SCORE = 7036   
    
def reindeer_maze():
    global maze
    start = (len(maze)-2, 1)
    scores = dict()
    visited = set()
    paths = set()
    min_score = 0
    queue = []
    queue.append((start[0], start[1], 0, ">", set()))
    while len(queue) > 0:
        r, c, score, direction, v = queue.pop()
        while maze[r][c] != "E":
            if ((r, c, direction) in visited and scores[(r, c, direction)] < score):
                break
            visited.add((r, c, direction))
            scores[(r, c, direction)] = score
            v.add((r, c))
            if direction == ">" or direction == "<":
                if min_score == 0 or score+1001 < min_score:
                    if maze[r+1][c] != "#":
                        queue.append((r+1, c, score+1001, "v", v.copy()))
                    if maze[r-1][c] != "#":
                        queue.append((r-1, c, score+1001, "^", v.copy()))
                if direction == ">" and maze[r][c+1] != "#":
                    score += 1
                    c += 1
                elif direction == "<" and maze[r][c-1] != "#":
                    score += 1
                    c -= 1
                else:
                    break
            else:
                if min_score == 0 or score+1001 < min_score:
                    if maze[r][c+1] != "#":
                        queue.append((r, c+1, score+1001, ">", v.copy()))
                    if maze[r][c-1] != "#":
                        queue.append((r, c-1, score+1001, "<", v.copy()))
                if direction == "^" and maze[r-1][c] != "#":
                    score += 1
                    r -= 1
                elif direction == "v" and maze[r+1][c] != "#":
                    score += 1
                    r += 1
                else:
                    break
            if maze[r][c] == "E":
                if score == BEST_SCORE: # PART 2
                    paths = paths | v
                    print(f"made it to the end with score = {score} in {len(v)+1} steps; {len(paths)+1} total")
                if (min_score == 0 or score < min_score):
                    min_score = score
    print(min_score)

reindeer_maze()        