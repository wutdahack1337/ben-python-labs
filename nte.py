s = input()

for char in s:
    if char:
        print(f"{char} : Yes" if char != " "
                                else f"{char} : No")
