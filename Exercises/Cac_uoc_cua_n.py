n = int(input())

for cac_so in range(1,n+1):
    if n%cac_so == 0:
        print(cac_so, end= " ")
    else:
        continue 