# The Minion Game

VOWELS = 'A E I O U'.split()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.substrings = set()

    def __str__(self):
        return f'{self.name} {self.score}'

    def add_score(self, score):
        self.score += score

    def add_substring(self, substring):
        self.substrings = self.substrings | set([substring]) - set([''])

def minion_game(string):
    stuart = Player('Stuart')
    kevin = Player('Kevin')

    substrings = lambda substring: sum(1 for i in range(0, len(string)-len(substring)+1) if string[i:i+len(substring)] == substring)

    for initial_letter in range(len(string)):
        
        if string[initial_letter] not in VOWELS:
            # Stuart
            for range_substring in range(initial_letter, len(string)+1):
                stuart.add_substring(string[initial_letter:range_substring])
        else:
            # Kevin
            for range_substring in range(initial_letter, len(string)+1):
                kevin.add_substring(string[initial_letter:range_substring])
    else:
        print(stuart.substrings)
        print(kevin.substrings)
        stuart.add_score(sum(substrings(substring) for substring in stuart.substrings))
        kevin.add_score(sum(substrings(substring) for substring in kevin.substrings)) 

    print(stuart if stuart.score > kevin.score else kevin)

if __name__ == '__main__':
    s = input()
    minion_game(s)
