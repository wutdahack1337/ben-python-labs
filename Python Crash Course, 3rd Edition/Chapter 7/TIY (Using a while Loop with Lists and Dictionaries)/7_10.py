responses = {}
polling_active = True

while polling_active:
    name = input("What's your name: ")
    place = input("If you could, where would you like to go?: ")

    responses[name] = place
    
    repeat = input("Would you like to let another person respond? (yes/no): ")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
print()
for name,place in responses.items():
    print(f"{name} ➜  {place}")
