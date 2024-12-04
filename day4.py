f = open('input_files/day4.txt')
wordsearch = []
for line in f:
    wordsearch.append(line)
f.close()

def find_XMAS(r: int, c: int) -> int:
    # given the index of a cell containing 'X', find all instances of 'XMAS' starting from there
    count = 0
    # look forward and backward
    if c+3 < len(wordsearch[r]) and wordsearch[r][c:c+4] == "XMAS":
        count += 1
    if c-3 >= 0 and wordsearch[r][c-3:c+1] == "SAMX":
        count += 1
    if r+3 < len(wordsearch):   # look down
        test_str = "X" + wordsearch[r+1][c] + wordsearch[r+2][c] + wordsearch[r+3][c]
        if test_str == "XMAS":
            count += 1  
        if c+3 < len(wordsearch[r+3]):    # diagonal down and forward
            test_str = "X" + wordsearch[r+1][c+1] + wordsearch[r+2][c+2] + wordsearch[r+3][c+3]
            if test_str == "XMAS":
                count += 1
        if c-3 >= 0:    # diagonal down and backward
            test_str = "X" + wordsearch[r+1][c-1] + wordsearch[r+2][c-2] + wordsearch[r+3][c-3]
            if test_str == "XMAS":
                count += 1
    if r-3 >= 0:   # look up
        test_str = "X" + wordsearch[r-1][c] + wordsearch[r-2][c] + wordsearch[r-3][c]
        if test_str == "XMAS":
            count += 1
        if c+3 < len(wordsearch[r]):    # diagonal up and forward
            test_str = "X" + wordsearch[r-1][c+1] + wordsearch[r-2][c+2] + wordsearch[r-3][c+3]
            if test_str == "XMAS":
                count += 1
        if c-3 >= 0:    # diagonal up and backward
            test_str = "X" + wordsearch[r-1][c-1] + wordsearch[r-2][c-2] + wordsearch[r-3][c-3]
            if test_str == "XMAS":
                count += 1
    return count

def find_X_MAS(r: int, c: int) -> bool:
    # given the index of a cell containing 'A', find if it's the centre of an X-MAS
    if r-1 < 0 or r+1 >= len(wordsearch) or c-1 < 0 or c+1 >= len(wordsearch):
        return False
    if wordsearch[r-1][c-1] == "M" and wordsearch[r+1][c+1] == "S":
        if wordsearch[r-1][c+1] == "M" and wordsearch[r+1][c-1] == "S":
            return True
        if wordsearch[r-1][c+1] == "S" and wordsearch[r+1][c-1] == "M":
            return True
    if wordsearch[r-1][c-1] == "S" and wordsearch[r+1][c+1] == "M":
        if wordsearch[r-1][c+1] == "M" and wordsearch[r+1][c-1] == "S":
            return True
        if wordsearch[r-1][c+1] == "S" and wordsearch[r+1][c-1] == "M":
            return True
    return False

result = 0
for r in range(len(wordsearch)):
    for c in range(len(wordsearch[r])):
        # if wordsearch[r][c] == "X":       # PART 1
        #     result += find_XMAS(r, c)
        if wordsearch[r][c] == "A" and find_X_MAS(r, c):    # PART 2
            result += 1
print(result)