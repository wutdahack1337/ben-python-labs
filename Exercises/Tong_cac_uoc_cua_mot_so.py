n = int(input())
ans = 0

for cac_so in range(1,n+1):
    if n%cac_so == 0:
        ans += cac_so
    else:
        continue 

print(ans)