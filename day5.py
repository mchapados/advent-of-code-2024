f = open('input_files/day5.txt')
rules = []
updates = []
for line in f:
    if "|" in line:
        rules.append(line.strip())
    elif "," in line:
        updates.append(line.strip())
f.close()

def check_order(update: str) -> int:
    # check if page numbers are in the right order according to the rules; if so, return middle number (else return 0)
    pages = update.split(',')
    for i in range(len(pages)):
        for j in range(i, len(pages)):
            # check each rule pertaining to i and j and confirm that i should come before j
            # or really that there isn't a rule stating that j comes before i
            if pages[j]+"|"+pages[i] in rules:
                return 0
    return int(pages[len(pages)//2])

def fix_order(update: str) -> int:
    # check if page numbers are in the right order according to the rules; if not, fix, then return middle number
    pages = update.split(',')
    fixed = False
    for i in range(len(pages)):
        for j in range(i, len(pages)):
            # if i and j are in the wrong order, swap them
            if pages[j]+"|"+pages[i] in rules:
                fixed = True
                pages[i], pages[j] = pages[j], pages[i]
    return int(pages[len(pages)//2]) if fixed else 0

result = 0
for u in updates:
    # result += check_order(u)      # PART 1
    result += fix_order(u)          # PART 2
print(result)