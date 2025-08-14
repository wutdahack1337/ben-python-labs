n = int(input())

day = 1
h = n//60
m = n - h*60

if n < 1440:
    print(h, m)
else:
    while h > 23:
        h -= 24
        day += 1

    while m > 1440:
        m -= 1440
    print(h, m)