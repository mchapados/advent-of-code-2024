f = open('input_files/day10.txt')
map = []
for line in f:
    map.append(list(line.strip()))
f.close()

class trailhead:
    def __init__(self):
        self.end = set()
        self.rating = 0
    def __add__(self, other):
        self.end = self.end | other.end
        self.rating += other.rating
        return self
    def score(self) -> int:
        return len(self.end)

def bfs(r: int, c: int):
    res = trailhead()
    if map[r][c] == "9":
        res.end.add((r, c))
        res.rating += 1
        return res
    else:
        if r-1 >= 0 and int(map[r-1][c]) == int(map[r][c])+1:
            res += bfs(r-1, c)
        if r+1 < len(map) and int(map[r+1][c]) == int(map[r][c])+1:
            res += bfs(r+1, c)
        if c-1 >= 0 and int(map[r][c-1]) == int(map[r][c])+1:
            res += bfs(r, c-1)
        if c+1 < len(map[0]) and int(map[r][c+1]) == int(map[r][c])+1:
            res += bfs(r, c+1)
        return res

result = 0
for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == "0":
            result += bfs(row, col).rating    # .score()   # PART 1
print(result)