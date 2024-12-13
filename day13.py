from sympy import symbols, Eq, solve

class claw_machine:
    def __init__(self, A = (0,0), B = (0,0), prize = (0,0)):
        self.A = A
        self.B = B
        self.prize = prize

    def cost(self, pt2 = False) -> int:
        if pt2:
            self.prize = self.prize[0]+10000000000000, self.prize[1]+10000000000000
        A, B = symbols('A B', integer=True)
        eq1 = Eq(self.A[0]*A + self.B[0]*B, self.prize[0])
        eq2 = Eq(self.A[1]*A + self.B[1]*B, self.prize[1])
        solution = solve((eq1, eq2), (A, B), dict=True, positive=True)
        costs = []
        for sol in solution:
            costs.append(3*sol[A]+sol[B])
        return min(costs) if len(costs) > 0 else 0

f = open('input_files/day13.txt')
claws = []
for line in f:
    x = line.find("X")
    y = line.find("Y")
    if "A" in line:
        claws.append(claw_machine())
        claws[-1].A = (int(line[x+2:line.find(",")]), int(line[y+2:]))
    elif "B" in line:
        claws[-1].B = (int(line[x+2:line.find(",")]), int(line[y+2:]))
    elif "Prize" in line:
        claws[-1].prize = (int(line[x+2:line.find(",")]), int(line[y+2:]))
f.close()

result = 0
for c in claws:
    result += c.cost(True)
print(result)