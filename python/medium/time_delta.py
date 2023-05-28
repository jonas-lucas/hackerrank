# Time Delta

import math
import os
import random
import re
import sys
from datetime import datetime, timedelta, timezone

MONTHS = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()

def return_time(t: str) -> datetime:
    elements = t.split()[1::]
    time_zone = timezone(
        -timedelta(
            hours=int(elements[4][1:3]),
            minutes=int(elements[4][3:5]),
        ) if elements[4][0] == '-' else
        timedelta(
            hours=int(elements[4][1:3]),
            minutes=int(elements[4][3:5]),
        )
    )
    date_time = datetime(
        year=int(elements[2]),
        month=int(MONTHS.index(elements[1]) + 1),
        day=int(elements[0]),
        hour=int(elements[3][0:2]),
        minute=int(elements[3][3:5]),
        second=int(elements[3][6:8]),
        tzinfo=time_zone,
    )
    return date_time

def time_delta(t1: str, t2: str) -> str:
    delta = return_time(t1) - return_time(t2)
    return str(abs(int(delta.total_seconds())))

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
