# 3_4:
guests = ['cow', 'dog', 'cat']

for guest in guests:
    print(f"{guest.title()}, do you want to have dinner with me? ")

print("\nUnfortunately, the Dog cannot come.\n")

guests.remove('dog') 

guests.append('wolf')

for guest in guests:
    print(f"{guest.title()}, do you want to have dinner with me? ")


