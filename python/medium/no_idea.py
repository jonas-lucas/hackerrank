# No Idea!

n, m = map(int, input().split())

array: list[int] = list(map(int, input().split()))

a: set[int] = set()
b: set[int] = set()

a |= set(map(int, input().split()))
b |= set(map(int, input().split()))

happiness: int = 0

for i in array:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1
        
print(happiness)
