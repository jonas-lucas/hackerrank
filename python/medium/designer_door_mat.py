import math

n, m = map(int, input().split())

for i in range(n):
    if i == n // 2:
        print('WELCOME'.center(m, '-'), end='')
    else:
        for j in range(m - (3 * (i + 1))): # 18, 15, 11
            if j == (m - (3 * (i + 1))) // 2:
                print('.|.' * (i + 1) if i % 2 == 0 else '.|.' * (i + 2), end='') # 1, 3, 5, 
            else:
                print('-', end='')
    print()