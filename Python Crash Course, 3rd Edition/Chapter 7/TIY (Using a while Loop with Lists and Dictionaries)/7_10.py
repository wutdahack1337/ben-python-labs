responses = {}

polling = True

while polling:
    name = input("What's your name?")
    place = input("If you could visit one place in the world, where would you go?")

    responses[name] = place

    repeat = input('Do you want to go anywhere else (yes/no)')