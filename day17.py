program = [2,4,1,1,7,5,4,4,1,4,0,3,5,5,3,0]
pointer = 0
operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: 202991746427434, 5: 0, 6: 0}

def adv(x): # 0
    global operands
    operands[4] = int(operands[4]//2**x)

def bxl(x): # 1
    global operands
    operands[5] = operands[5] ^ x

def bst(x): # 2
    global operands
    operands[5] = x % 8

def jnz(x): # 3
    global operands
    global pointer
    if operands[4] != 0:
        pointer = x - 2

def bxc(x): # 4
    global operands
    operands[5] = operands[5] ^ operands[6]

def out(x): # 5
    return x % 8

def bdv(x): # 6
    global operands
    operands[5] = int(operands[4]//2**x)

def cdv(x): # 7
    global operands
    operands[6] = int(operands[4]//2**x)

opcodes = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

output = []
while pointer < len(program):
    code = program[pointer]
    x = program[pointer+1]
    if code == 5:
        output.append(out(operands[x]))
    elif code == 1 or code == 3:
        opcodes[code](x)
    else:
        opcodes[code](operands[x])
    pointer += 2
print(output)