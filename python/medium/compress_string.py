# Compress the String!

from itertools import groupby

s: str = input()

print(' '.join(map(str, [(len(list(y)), int(x)) for x, y in groupby(s)])))
