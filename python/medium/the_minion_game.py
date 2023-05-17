# The Minion Game

VOWELS = ['A', 'E', 'I', 'O', 'U']

def minion_game(string):
    stuart = 0
    kevin = 0
    length = len(string)

    for i, char in enumerate(string):
        if char in VOWELS:
            kevin += length - i
        else:
            stuart += length - i

    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
