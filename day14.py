import numpy as np

WIDTH, HEIGHT = 101, 103

class robot:
    def __init__(self, p = [0,0], v = [0,0]):
        self.p = p
        self.v = v

    def move(self, s = 1):
        self.p[0] += self.v[0] * s
        while self.p[0] < 0:
            self.p[0] = WIDTH + self.p[0]
        while self.p[0] >= WIDTH:
            self.p[0] = self.p[0] - WIDTH
        self.p[1] += self.v[1] * s
        while self.p[1] < 0:
            self.p[1] = HEIGHT + self.p[1]
        while self.p[1] >= HEIGHT:
            self.p[1] = self.p[1] - HEIGHT

f = open('input_files/day14.txt')
robots = []
for line in f:
    p, v = line.split(" ")
    p_x, p_y = int(p[2:p.find(",")]), int(p[p.find(",")+1:])
    v_x, v_y = int(v[2:v.find(",")]), int(v[v.find(",")+1:])
    robots.append(robot([p_x, p_y], [v_x, v_y]))
f.close()

# simulate robot movement for 100 seconds
# and add all robots' final positions to the grid
grid = np.zeros((HEIGHT, WIDTH), dtype=int)
for r in robots:
    r.move(100)
    grid[r.p[1]][r.p[0]] += 1

# count the number of robots in each quadrant
q = [0, 0, 0, 0]
for row in range(HEIGHT):
    for col in range(WIDTH):
        if row < HEIGHT//2:
            if col < WIDTH//2:
                q[0] += grid[row][col]
            elif col > WIDTH//2:
                q[1] += grid[row][col]
        elif row > HEIGHT//2:
            if col < WIDTH//2:
                q[2] += grid[row][col]
            elif col > WIDTH//2:
                q[3] += grid[row][col]

result = int(q[0] * q[1] * q[2] * q[3])
print(result)

def christmas_tree() -> bool:
    grid = np.zeros((HEIGHT, WIDTH), dtype=int)
    for r in robots:
        grid[r.p[1]][r.p[0]] += 1
    result = np.count_nonzero(grid)
    return True if result == 500 else False

seconds = 100
while not christmas_tree():
    for r in robots:
        r.move(1)
    seconds += 1
print(seconds)