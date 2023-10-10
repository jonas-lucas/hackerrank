# Triangle Quest 2

# My Answers:
# for i in range(1, int(input())+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     for j in range(i-1, 0, -1):
#         print(j, end='')
#     print()

# for i in range(1, int(input())+1):
#     print(''.join(map(str, range(1, i+1))) + ''.join(map(str, range(i-1, 0, -1))))

for i in range(1, int(input())+1):
    print((10 ** i - 1) ** 2 // 81)