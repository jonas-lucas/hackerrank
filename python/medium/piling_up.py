# Piling Up!

t: int = int(input())

for _ in range(t):
    n: int = int(input())
    blocks: list[int] = list(map(int, input().split()))
        
    block: int
        
    if blocks[0] >= blocks[-1]:
        block = blocks.pop(0)
    else:
        block = blocks.pop(-1)
        
    while blocks:
        if blocks[0] >= blocks[-1] and blocks[0] <= block:
            block = blocks.pop(0)
        elif blocks[0] < blocks[-1] and blocks[-1] <= block:
            block = blocks.pop(-1)
        else:
            print('No')
            break
    else:
        print('Yes')
