f = open('input_files/day19.txt')
towels = []
designs = []
for line in f:
    if len(towels) == 0:
        towels = line.split(", ")
    elif line != "\n":
        designs.append(line.strip())
f.close()

class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word, start):
        node = self.root
        for i in range(start, len(word)):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            if node.is_end_of_word:
                yield i + 1  # Return the end index of a valid substring

towel_trie = Trie()
for t in towels:
    towel_trie.insert(t)

def possible(design) -> int:
    global towel_trie
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # Empty string is always valid

    for i in range(len(design)):
        if dp[i] > 0:  # if position i can be reached
            for end in towel_trie.search(design, i):
                dp[end] += dp[i]
    return dp[len(design)]

result = 0
ways = 0
for d in designs:
    p = possible(d)
    if p > 0:
        result += 1
        ways += p
print(result)
print(ways)