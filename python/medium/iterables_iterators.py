# Iterables and Iterators

from itertools import combinations

n: int = int(input())

lst: list[str] = input().split()

k: int = int(input())

comb: list[tuple] = list(combinations(lst, k))
total: int = len(comb)
a: int = 0
for pos in comb:
    if 'a' in pos:
        a += 1

print(f'{a/total}')