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