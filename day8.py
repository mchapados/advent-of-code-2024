from collections import defaultdict

f = open('input_files/day8.txt')
map = []
for line in f:
    map.append(list(line.strip()))
f.close()

# create a list of antennas for each frequency
antenna_list = defaultdict(list)
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] != ".":
            antenna_list[map[r][c]].append([r, c])

def find_antinodes(part2 = False):
    for key in antenna_list:
        # for each frequency, for each pair of antennas, add their antinodes to the map
        if len(antenna_list[key]) >= 2:
            for i in range(len(antenna_list[key])):
                for j in range(i+1, len(antenna_list[key])):
                    a, b = antenna_list[key][i], antenna_list[key][j]
                    row_diff = a[0] - b[0]
                    col_diff = a[1] - b[1]
                    if not part2:
                        # if the new antinodes are on the map, add them
                        if a[0]+row_diff >= 0 and a[0]+row_diff < len(map) and a[1]+col_diff >= 0 and a[1]+col_diff < len(map[0]):
                            map[a[0]+row_diff][a[1]+col_diff] = "#"
                        if b[0]-row_diff >= 0 and b[0]-row_diff < len(map) and b[1]-col_diff >= 0 and b[1]-col_diff < len(map[0]):
                            map[b[0]-row_diff][b[1]-col_diff] = "#"
                    else:
                        # for each cell on the line with that slope, add an antinode
                        cur_row, cur_col = a[0], a[1]
                        while cur_row >= 0 and cur_row < len(map) and cur_col >= 0 and cur_col < len(map[0]):
                            map[cur_row][cur_col] = "#"
                            cur_row += row_diff
                            cur_col += col_diff
                        cur_row, cur_col = b[0], b[1]
                        while cur_row >= 0 and cur_row < len(map) and cur_col >= 0 and cur_col < len(map[0]):
                            map[cur_row][cur_col] = "#"
                            cur_row -= row_diff
                            cur_col -= col_diff

find_antinodes(True)
result = 0
for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == "#":
            result += 1
print(result)