import numpy as np

f = open('input_files/day12.txt')
map = []
for line in f:
    map.append(list(line.strip()))
f.close()

visited = np.zeros((len(map), len(map[0])))

class region:
    def calc_region(self, plant: str, r: int, c: int) -> int:
        visited[r][c] = 1
        area = 1
        if r == 0 or r == len(map)-1:
            if r == 0: self.edges.append(("top", r, c))
            else: self.edges.append(("bottom", r, c))
        if r > 0 and map[r-1][c] != plant:
            self.edges.append(("top", r, c))
        if r < len(map)-1 and map[r+1][c] != plant:
            self.edges.append(("bottom", r, c))
        if c == 0 or c == len(map[0])-1:
            if c == 0: self.edges.append(("left", r, c))
            else: self.edges.append(("right", r, c))
        if c > 0 and map[r][c-1] != plant:
            self.edges.append(("left", r, c))
        if c < len(map[0])-1 and map[r][c+1] != plant:
            self.edges.append(("right", r, c))

        if c+1 < len(map[0]) and map[r][c+1] == plant and not visited[r][c+1]:
            area += self.calc_region(plant, r, c+1)
        if r+1 < len(map) and map[r+1][c] == plant and not visited[r+1][c]:
            area += self.calc_region(plant, r+1, c)
        if c-1 >= 0 and map[r][c-1] == plant and not visited[r][c-1]:
            area += self.calc_region(plant, r, c-1)
        if r-1 >= 0 and map[r-1][c] == plant and not visited[r-1][c]:
            area += self.calc_region(plant, r-1, c)
        return area

    def calc_sides(self) -> int:
        self.edges.sort()
        for edge in self.edges:
            if edge[0] == "bottom" or edge[0] == "top":
                r, c = edge[1], edge[2]
                while (edge[0], r, c+1) in self.edges:
                    self.edges.remove((edge[0], r, c+1))
                    c += 1
            if edge[0] == "left" or edge[0] == "right":
                r, c = edge[1], edge[2]
                while (edge[0], r+1, c) in self.edges:
                    self.edges.remove((edge[0], r+1, c))
                    r += 1
        return len(self.edges)

    def __init__(self, plant, r, c):
        self.edges = []
        self.area = self.calc_region(plant, r, c)
        self.perimeter = len(self.edges)
        self.sides = self.calc_sides()

    def price(self, pt2 = False):
        if pt2:
            return self.area * self.sides
        return self.area * self.perimeter

result = 0
for row in range(len(map)):
    for col in range(len(map[row])):
        if not visited[row][col]:
            new_region = region(map[row][col], row, col)
            result += new_region.price(True)
print(result)