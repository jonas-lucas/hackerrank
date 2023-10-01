# Word Order

from collections import Counter

n: int = int(input())

cntr: Counter = Counter()

for _ in range(n):
    cntr[input()] += 1
    
print(len(cntr))
print(' '.join(map(str, [cntr[x] for x in cntr])))
