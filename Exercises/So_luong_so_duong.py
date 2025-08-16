a, b, c = map(int, input().split())
ans = 0
ds = [a, b, c]

for num in ds:
    if num > 0:
        ans += 1

print(ans)