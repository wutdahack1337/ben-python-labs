s = int(input())
tong_cs = 0
sl_cs = 0

while s != 0:
    tong_cs += s%10
    s = s//10
    sl_cs += 1
    
print(tong_cs)
print(sl_cs)
