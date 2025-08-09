# 3_4:
guests = ['cow', 'dog', 'cat']

for guest in guests:
    print(f"{guest.title()}, do you want to have dinner with me? ")
    
# 3_5:
print("\nUnfortunately, the Dog cannot come.\n")

guests.remove('dog') 

guests.append('wolf')

for guest in guests:
    print(f"{guest.title()}, do you want to have dinner with me? ")

# 3_6:
print("\nLuckily, we just got a bigger table so we will have more people.\n")

guests.insert(0, 'fish')
guests.insert(2, 'fox')
guests.append('bear')

for guest in guests:
    print(f"{guest.title()}, do you want to have dinner with me? ")

# 3_7:
print("\nUnfortunately, the table won't be delivered on time, so there's only room for two.\n")

# Xóa đến khi nào chỉ còn 2 khách


print(f"Sorry {guests[-1]}, you can't come") #1
guests.pop()
print(f"Sorry {guests[-1]}, you can't come") #2
guests.pop()
print(f"Sorry {guests[-1]}, you can't come") #3
guests.pop()
print(f"Sorry {guests[-1]}, you can't come")  #4
guests.pop()

print(f"\n{guests[-1]}, you're still invited")
print(f"{guests[-2]}, you're still invited")

del guests[0]
del guests[-1]

print(guests)


