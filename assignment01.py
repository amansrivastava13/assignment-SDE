a = ["-214748364801","-214748364802"]

import sys


def get_second_max(a):
    if len(a) < 2:
        return -1
    max_ = int(a[0])
    second_max = - sys.maxsize
    for num in a[1:]:
        temp = int(num)
        if temp > max_:
            second_max = max_
            max_ = temp

        elif temp > second_max and temp < max_:
            second_max = temp

    if second_max == -sys.maxsize:
        second_max = -1
    return second_max


second_max = get_second_max(a)
print(second_max)
