# Maxizime It!

from itertools import product

k: int
m: int

k, m = map(int, input().split())
s: list[int] = []
for _ in range(k):
    s.append(list(map(int, input().split()))[1:])

lst: list[int] = []
for p in product(*s):
    lst.append(sum(map(lambda x: x**2, p)) % m)

print(max(lst))
