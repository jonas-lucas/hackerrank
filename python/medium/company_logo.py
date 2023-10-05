# Company Logo

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s: str = input()
    
    counter: Counter = Counter(s)
    
    lst: list[tuple[str, int]] = sorted(
        sorted(
            [(key, counter[key]) for key in counter]
        ), key=lambda x: x[1], reverse=True
    )
        
    for i in range(3):
        print(f'{lst[i][0]} {lst[i][1]}')