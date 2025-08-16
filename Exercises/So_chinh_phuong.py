import math

n = abs(int(input()))

can = int(math.sqrt(n))
if can*can == n:
    print(1)
else:
    print(0)