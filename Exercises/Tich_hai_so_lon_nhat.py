a, b, c = map(int, input().split())
ds = [a, b, c]

#Cach1
cap_ab = a*b
cap_ac = a*c
cap_bc = b*c

if cap_ab >= cap_ac and cap_ab >= cap_bc:
    print(cap_ab)
elif cap_ac >= cap_ab and cap_ac >= cap_bc:
    print(cap_ac)
else:
    print(cap_bc)

#Cach2

print(max(ds[0] * ds[1], ds[1] * ds[2]))
