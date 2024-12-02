f = open('input_files/day1.txt')
left = []
right = []
for line in f:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))
f.close()

def part1():
    # sort the lists, then sum the differences between each item
    left.sort()
    right.sort()
    result = 0  
    for i in range(len(left)):
        result += abs(left[i]-right[i])
    print(result)

def part2():
    # for each number in left, count how many times it appears in right
    # multiply the value by the count, add to result
    result = 0
    for val in left:
        result += val * right.count(val)
    print(result)

# part1()
part2()