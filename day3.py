f = open('input_files/day3.txt')
memory = f.read()
f.close()

# scan memory to find all strings conforming to mul(x, y)
# where x and y are 1-3 digit integers
# perform all the muliplications and sum the results

def part1():
    result = 0
    i = 0
    while i < len(memory):
        i = memory.find('mul(', i)
        if i < 0:
            break
        j = memory.find(')', i+6, i+12)
        if j > 0:
            try:
                x, y = memory[i+4:j].split(',')
                result += int(x) * int(y)
            except:
                pass
        i += 4
    print(result)

def part2():
    result = 0
    i = 0
    while i < len(memory):
        stop = memory.find("don't()", i) # find the next don't
        stop = stop if stop > 0 else len(memory)
        while i < stop:
            i = memory.find('mul(', i) # find the next mul
            if i < 0 or i > stop:
                break
            j = memory.find(')', i+6, i+12)
            if j > 0:
                try:
                    x, y = memory[i+4:j].split(',') # if we get here, it is a real mul instruction
                    result += int(x) * int(y)
                except:
                    pass
            i += 4
        # now we're either at a don't() or at the end, so find the next do()
        i = memory.find('do()', i)
        if i < 0:
            break
    print(result)

part2()