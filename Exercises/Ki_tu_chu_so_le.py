s= input()
s_list= list(s)
ans = 0

for char in s_list:
    num= int(char)
    if int(char)%2 != 0:
        ans += 1
    else:
        continue
print(ans)