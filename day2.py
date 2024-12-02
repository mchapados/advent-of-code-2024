f = open('input_files/day2.txt')
reports = []
for line in f:
    reports.append(line)
f.close()

def is_safe(levels) -> bool:
    increasing = True if levels[1] > levels[0] else False
    for i in range(len(levels)-1):
        if increasing and levels[i+1] <= levels[i]:
            return False
        if not increasing and levels[i+1] >= levels[i]:
            return False
        if abs(levels[i]-levels[i+1]) > 3 or abs(levels[i]-levels[i+1]) < 1:
            return False
    return True

def is_safe_pt2(levels) -> bool:
    increasing = True if levels[1] > levels[0] else False
    problem = False
    for i in range(len(levels)-1):
        if increasing and levels[i+1] <= levels[i]:
            problem = True
            break
        if not increasing and levels[i+1] >= levels[i]:
            problem = True
            break
        if abs(levels[i]-levels[i+1]) > 3 or abs(levels[i]-levels[i+1]) < 1:
            problem = True
            break
    if problem:
        for i in range(len(levels)):
            ignore = levels.pop(i)
            if is_safe(levels):
                return True
            levels.insert(i, ignore)
        return False
    return True

def check_safety(part1 = True):
    result = 0
    for r in reports:
        levels = r.split()
        levels = [int(i) for i in levels]
        safety = is_safe(levels) if part1 else is_safe_pt2(levels)
        if safety:
            result += 1
    print(result)

check_safety(False)