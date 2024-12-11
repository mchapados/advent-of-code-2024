from collections import Counter

f = open('input_files/day11.txt')
stones = Counter(f.read().split())
f.close()

def blink(stones: Counter) -> Counter:
    res = Counter()
    res["1"] = stones["0"] # if 0, replace with 1 
    for key in stones:
        if len(key) % 2 == 0: # if even number of digits, split into 2, e.g. 1001 -> 10, 1
            res[key[:len(key)//2]] += stones[key]
            res[str(int(key[len(key)//2:]))] += stones[key]
        elif key != "0": # else, replace with value * 2024
            res[str(int(key)*2024)] += stones[key]
    return res

for _ in range(75):
    stones = blink(stones)
print(stones.total())