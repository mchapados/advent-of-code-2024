f = open('input_files/day9.txt')
disk_map = f.read()
f.close()

filesystem = []
file_id = 0
for i in range(len(disk_map)):
    blocks = int(disk_map[i])
    if i % 2 == 0: # even indexes are files
        for j in range(blocks):
            filesystem.append(str(file_id))
        file_id += 1
    else: # free space
        for j in range(blocks):
            filesystem.append(".")

def part1():
    i, j = 0, len(filesystem)-1
    while i < j:
        while filesystem[i] != ".": # increment i until we get to a free space
            i += 1
        while filesystem[j] == ".": # decrement j until we get to a file
            j -= 1
        if i < j:   # swap
            filesystem[i], filesystem[j] = filesystem[j], filesystem[i] 

def part2():
    file_map_id = len(disk_map)-2 if (len(disk_map) % 2 == 0) else len(disk_map)-1
    for file in range(file_id-1, 0, -1): # for each file in decreasing order, find the left-most free space that can hold it
        size = int(disk_map[file_map_id])
        for i in range(len(filesystem)): # move pointer up to the first free space
            if filesystem[i] == str(file): # if we get to the file we're trying to move, stop
                break
            if filesystem[i] == ".": # check if free space is the correct size
                can_move = True
                for j in range(i+1, i+size):
                    if filesystem[j] != ".":
                        can_move = False
                        break
                if can_move:    # swap file into free space
                    file_index = filesystem.index(str(file))
                    filesystem[i:i+size], filesystem[file_index:file_index+size] = filesystem[file_index:file_index+size], filesystem[i:i+size]
                    break
        file_map_id -= 2

part2()
result = 0  # multiply file ID by its position and sum
for i in range(len(filesystem)):
    if filesystem[i] == ".":
        continue    # break # PART 1
    result += i * int(filesystem[i])
print(result)