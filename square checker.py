from math import *
n = 432423
def is_square(n):
    if n < 0:
        return False
    new_n = sqrt(n)
    if int(new_n) * int(new_n) == n:
        return True
    else:
        return False
print(is_square(n))