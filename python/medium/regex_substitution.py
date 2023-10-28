# Regex Substitution

import re

n: int = int(input())

text: str = ''

for _ in range(n):
    text += input() + '\n'
 
# Replace && to and
text = re.sub(r'(?<= )&&(?= )', 'and', text)

# Replace || to or
text = re.sub(r'(?<= )\|\|(?= )', 'or', text)

print(text)
