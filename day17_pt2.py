program = [2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0]

def solve(A, n, sol):
    global program
    B = int(((A // 8**n)% 8) ^ 1)
    C = int((A // 8**n) / 2**B)
    res = int(((B ^ C) ^ 4) % 8)
    if n == len(program)-1:
        return res == sol
    if res == sol:
        return solve(A, n+1, program[n+1])
    return False

max_A = 211106232532992
a = 175921860444160
for i in range(len(program)-1, -1, -1):
    while a <= max_A:
        if solve(a, i, program[i]):
            print(f"solved n = {i} with A = {a}")
            break
        a += 8**i