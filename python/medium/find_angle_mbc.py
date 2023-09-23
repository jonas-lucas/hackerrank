# Finde Angle MBC

import math

ab: int = int(input())

bc: int = int(input())

teta: int = round(math.degrees(math.atan(ab/bc)))

print(str(teta) + chr(176))